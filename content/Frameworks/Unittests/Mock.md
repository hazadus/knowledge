# Testing with Python (part 6): Fake it...

🔗 [Source](https://www.bitecode.dev/p/testing-with-python-part-6-fake-it)

Mocks, also called test doubles, are objects dedicated to faking a behavior, so that you can write unit tests that depend on other parts of the code, without running said code.

Indeed, if I have a function that delegates behavior to 3 other functions:

    def transform(param):
        return param * 2
    
    def check(param):
        return "bad" not in param
    
    def calculate(param):
        return len(param)
    
    def main(param, option):
        if option:
            param = transform(param)
        if not check(param):
            raise ValueError("Woops")
        return calculate(param)

I can test `main()` in two ways:

*   Create an integration test that will call the function, exercise the whole chain of calls, and get the real value.
    
*   Create a unit test that will call the function, and check that it delegates what we expect it to delegate.
    

As we have discussed in previous articles, both approaches have pros and cons, but the consequences of each will appear more clearly with examples.

I'm not going to debate again how to choose which and which, but as a professional, you should know how to do both, so you can choose which one matches your goals and constraints.

To implement the second strategy, we would need mocks to fake `transform()`, `check()` and `calculate()`.

Mocks can be used in two ways, as objects and as functions. It's the same, really, because functions are objects in Python, but it's easier to learn about them if we make this distinction.

First, as functions.

You can create a fake function, and call it with any parameter you want, it will always work, and by default return a new mock:

    >>> from unittest.mock import Mock
    >>> a_fake_function = Mock()
    >>> a_fake_function()
    <Mock name='mock()' id='140204477912480'>
    >>> a_fake_function(1, "hello", option=True)
    <Mock name='mock()' id='140204477912480'>

To make it more useful, we can decide what the function should return, or if it should raise an exception. Those fake results are also known as “stubs":

    >>> another_one = Mock(return_value="tada !")
    >>> another_one()
    'tada !'
    >>> a_broken_one = Mock(side_effect=TypeError('Nope'))
    >>> a_broken_one()
    Traceback (most recent call last):
    ...
    TypeError: Nope

`side_effect` can also be a callable if you want to generate the return value dynamically. Yes, it's weird it's not `return_value` that accepts a callable instead.

Mocks can be used like objects as well. Any attribute access that doesn't start with `_` returns a mock. If the attribute is a method, you can call it, and, well, you get back a mock...

    >>> from unittest.mock import Mock
    >>> mocking_bird = Mock()
    >>> mocking_bird.chip()
    <Mock name='mock.chip()' id='140204462793264'>
    >>> mocking_bird.foo(bar=1)
    <Mock name='mock.foo(bar=1)' id='140204460043296'>
    >>> mocking_bird.color
    <Mock name='mock.color' id='140204464845008'>
    >>> mocking_bird.name
    <Mock name='mock.name' id='140204477913536'>
    >>> mocking_bird.child.grand_child.whatever
    <Mock name='mock.child.grand_child.whatever' id='140204462902480'>

The `_` limitation means you can't index or add a mock without an explicit definition of the related dundder methods, though. To avoid this tedious process, use [MagicMock](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock), instead of Mock. Most of the time, you want `MagicMock` anyway so you probably are good using only that:

    >>> Mock()[0]
    Traceback (most recent call last):
    ...
    TypeError: 'Mock' object is not subscriptable
    
    >>> MagicMock()[0]
    <MagicMock name='mock.__getitem__()' id='140195073495472'>

And you can mix and match all those behaviors, since any param of MagicMock that is not reserved can be used to set an attribute:

    >>> reasonable_person = MagicMock(eat=Mock(return_value="chocolate"), name="Jack")
    >>> reasonable_person.name
    'Jack'
    >>> reasonable_person.eat(yum=True)
    'chocolate'
    >>>

If mocks were just a way to play make-believe, they would be only half useful for testing, but mocks also record calls made to them, so you can check if something happened:

    >>> reasonable_person.eat.call_args_list
    [call(yum=True)]
    >>> reasonable_person.eat.assert_called_with(yum=True) # passes
    >>> reasonable_person.eat.assert_called_with(wait="!") # doesn't pass
    Traceback (most recent call last):
    ...
    Actual: eat(yum=True)
    >>> reasonable_person.this_method_doesnt_exist.assert_called()
    Traceback (most recent call last):
    ...
    AssertionError: Expected 'this_method_doesnt_exist' to have been called.

While you can create mocks by hand, there are handy tools to do some of the heavy lifting for you.

You can automatically create a mock that matches another object shape with [create\_autospec()](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.create_autospec):

    >>> class AJollyClass:
    ...     def __init__(self):
    ...         self.gentlemanly_attribute = "Good day"
    ...         self.mustache = True
    >>> good_lord = create_autospec(AJollyClass(), spec_set=True)
    >>> good_lord.mustache
    <NonCallableMagicMock name='mock.mustache' spec_set='bool' id='131030999991728'>
    >>> good_lord.other
    Traceback (most recent call last):
    ...
    AttributeError: Mock object has no attribute 'other

It works with functions too:

    >>> def oh_my(hat="top"):
    ...     pass
    >>> by_jove = create_autospec(oh_my, spec_set=True)
    >>> by_jove(hat=1)
    <MagicMock name='mock()' id='131030900955296'>
    >>> by_jove(cat=1)
    Traceback (most recent call last):
    ...
    TypeError: got an unexpected keyword argument 'cat'

Finally, when you want to temporarily swap a real object with a mock, you can use [patch()](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch).

    >>> import requests
    >>> from unittest.mock import patch
    >>> with patch('__main__.requests'):
    ...     requests.get('http://bitecode.dev')
    ...
    <MagicMock name='requests.get()' id='140195072736224'>

This replaces the `requests` with a mock, but only in the `with` block.

`patch()` can also be used in a decorator form with the syntax `@patch('module1.function1')`, which is handy if you use pytest as we will see further down. It even can be used to substitute part of [a dict](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict) or [an object](https://docs.python.org/3/library/unittest.mock.html#patch-object)

`patch()` is a bit tricky to use because you have to pass a string that represents the dotted path of what you want to replace but **it must be where the thing is used, not where the thing is defined**. Hence the `__main__` here, because I patch the request that I use in my own module.

Confused?

Imagine I have a module `client.py` with this function:

    import requests
    def get_data():
        return requests.get(...)

If I use `patch` in a test, I should NOT do:

    with patch('requests'):
         get_data()

I should do:

    with patch('client.requests'):
         get_data()
    

Because I want to patch the reference of `requests` in that particular file, not in general.

Let's go back to our `main()` function:

    def main(param, option):
        if option:
            param = transform(param)
        if not check(param):
            raise ValueError('Woops')
        return calculate(param)

If I had to do an integration test, I would do:

    from my_life_work import main
    
    def test_main():
    
        assert main("param", False) == 5
        assert main("param", True) == 10
    
        with pytest.raises(ValueError):
            main("bad_param", False)

If I want to turn that into a unit test, then I would use mocks:

    import pytest
    
    from unittest.mock import patch
    from my_life_work import main
    
    # Careful! The order of patch is the reverse of the order of the params
    @patch("my_life_work.transform")
    @patch("my_life_work.check")
    @patch("my_life_work.calculate")
    def test_main(calculate, check, transform):
        check.return_value = True
        calculate.return_value = 5
    
        # We check that:
        # - transform() is not called if option is False
        # - check() verifies that the parameter is ok
        # - calculate() is called, its return value is the output of main()
        assert main("param", False) == calculate.return_value
        transform.assert_not_called()
        check.assert_called_with("param")
        calculate.assert_called_once_with("param")
    
        # Same thing, but transform() should be called, and hence check() 
        # should receive the transformed result
        transform.return_value = "paramparam"
        calculate.return_value = 10
        assert main("param", True) == calculate.return_value
        transform.assert_called_with("param")
        check.assert_called_with("paramparam")
        calculate.assert_called_with("paramparam")
    
        # We check that if the check fails, that raises the expected error
        # an nothing else is called.
        with pytest.raises(ValueError):
            check.side_effect = ValueError
            main("bad_param", False)
            check.assert_called_with("param")
            transform.assert_not_called()
            calculate.assert_not_called()

Now the test is isolated, fast, yet checks that our code fulfills the contracts of all the functions it depends on.

It's also verbose and more complicated.

I'll write a full article to explain why you may want to do this, when, and how. Because I understand that if you look at this type of test for the first time, it's not obvious why you would inflict this on yourself rather than the previous version.

Another problem with mocks is that if you type the wrong attribute name, you will not get an error.

It's easy to make mistakes, and it's very hard to find them when you do. A bunch of failsafes have been put in place, such as alerting you when you misspell `assert_*` or providing `create_autospec()`.

Nevertheless, I think that since mocks are already quite a complicated topic, and hard to manipulate, adding the possibility to mess up everything silently with a typo is too much for my taste.

At some point, you will be deep inside nested mocks with side effects and return values coming from a method of some patched object, and no, you will not have a good time.

