# Single and Double Underscores in Python Names – Real Python

![rw-book-cover](https://cdn.realpython.com/static/favicon.68cbf4197b0c.png)

## Metadata
- Author: [[Real Python]]
- Full Title: Single and Double Underscores in Python Names – Real Python
- Category: #articles
- Document Tags: [[python]] 
- Summary: Python uses single and double underscores in naming conventions to distinguish between public and non-public names in code, ensuring clarity and readability. Single leading underscores denote non-public names, while double leading underscores in classes trigger name mangling to avoid naming conflicts. Understanding and following these naming conventions is essential for writing Python code that is consistent and easily understandable by others.
- URL: https://realpython.com/python-double-underscore/

## Highlights
- The Python community uses the underscore character (`_`) as part of other naming conventions. Here’s a summary of what [PEP 8](https://peps.python.org/pep-0008/) says about using this character in names: ([View Highlight](https://read.readwise.io/read/01jdc0fhnyb4tb6t2t2fqtxbpy))

- Note that only two of these conventions enforce specific Python behaviors. Using double leading underscores triggers [name mangling](https://realpython.com/python-pep8/#naming-conventions) in Python classes. ([View Highlight](https://read.readwise.io/read/01jdc0fhyhz73hj7bzbe4xf5zq))

- Additionally, those names with double leading and trailing underscores that are listed in the Python [data model](https://docs.python.org/3/reference/datamodel.html) trigger internal behaviors in specific contexts. ([View Highlight](https://read.readwise.io/read/01jdc0fj2bf3pn3syw6gec55jy))

- In general, you should use a single leading underscore only when you need to indicate that a variable, class, method, function, or module is intended for internal use within the containing module, class, or package. Again, this is just a well-established naming convention. It’s not a strict rule that Python enforces. ([View Highlight](https://read.readwise.io/read/01jdc0fj7zg9zwr845hy9pak5c))

- In general, objects that you’re likely to change through the evolution of your code should remain non-public. So, when in doubt, give your objects non-public names. If you later decide that a given non-public object should become part of your code’s API, then you can remove the leading underscore. This practice lets you stabilize your API and prevent breaking your user’s code. ([View Highlight](https://read.readwise.io/read/01jdc0fjbqqyc7evwmm74c2fv8))

- Public attributes are those that you expect unrelated clients of your class to use, with your commitment to avoid backwards incompatible changes. Non-public attributes are those that are not intended to be used by third parties; you make no guarantees that non-public attributes won’t change or even be removed. ([View Highlight](https://read.readwise.io/read/01jdc0fjhehnreeh598s0g23n5))

- Even though you’ll find many resources out there that claim that name mangling is for creating private attributes, this naming transformation pursues a different goal: _preventing name clashes in inheritance_. To define non-public members, you should use a single leading underscore ([View Highlight](https://read.readwise.io/read/01jdc0fjn43gpsbgafffvf032h))

- To use wildcard imports properly, you should know that they don’t import non-public names. ([View Highlight](https://read.readwise.io/read/01jdc0fjtpdpnwb0m927nf4ran))

- Python enforces the above behavior. However, this behavior only applies to wildcard imports. You can still access non-public names using other import statement forms: ([View Highlight](https://read.readwise.io/read/01jdc0fjyf9dwpjga57e8g06k3))

- When you’re writing classes, sometimes it’s hard to decide whether an attribute should be public or non-public. This decision will depend on how you want users to use your classes. In most cases, attributes should be non-public to promote the safe use of your classes. ([View Highlight](https://read.readwise.io/read/01jdc0fk22752f5nvcw0s16wan))

- When you name an attribute or method using two leading underscores, Python automatically renames it by prefixing its name with the class name and a single leading underscore. This renaming process is known as **name mangling**. ([View Highlight](https://read.readwise.io/read/01jdc0fkagxem4744yhndnx7mm))

- Because of this internal renaming, you can’t access the attribute or method from outside the class using their original names: ([View Highlight](https://read.readwise.io/read/01jdc0fke4q96t116fjw31y55n))

- You can still access named-mangled attributes or methods using their mangled names, although this is bad practice, and you should avoid it in your code. If you see a name that uses this convention in someone’s code, then don’t try to force the code to use the name from outside its containing class. ([View Highlight](https://read.readwise.io/read/01jdc0fkj05p27vvtf8dk7vqwa))

- Name mangling is particularly useful when you want to ensure that a given attribute or method won’t be accidentally overridden in a subclass: ([View Highlight](https://read.readwise.io/read/01jdc0fkr8mr59gd7m3xe3dnk2))

- Another naming convention that you’ll find in Python code is to use a single trailing underscore. This convention comes in handy when you want to use a name that clashes with a Python keyword or a built-in name. In this situation, adding a trailing underscore will help you avoid the issue. ([View Highlight](https://read.readwise.io/read/01jdc0fkxgddh9w181m9br6qcr))

- In Python, names with double leading and trailing underscores (`__`) have special meaning to the language itself. These names are known as **dunder** names, and dunder is short for **d**ouble **under**score. In most cases, Python uses dunder names for methods that support a given functionality in the language’s [data model](https://docs.python.org/3/reference/datamodel.html). ([View Highlight](https://read.readwise.io/read/01jdc0fm3bmjqzkfjsx8a5qeg8))

- creating a custom dunder name won’t have a practical effect because Python only calls those special methods that the language defines. ([View Highlight](https://read.readwise.io/read/01jdc0fm7e95cg085xbg71ba7k))



----
📂 [[Articles]] | Последнее изменение: 23.11.2024 16:34