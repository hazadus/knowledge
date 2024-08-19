📂 [[Tooling]]

----
## Useful Stuff
`freezegun` **allows to emulate any date.**
https://github.com/spulec/freezegun
**Методы класса TestCase:**

> [!info] Обучающая онлайн-платформа Skillbox  
> Выберите свой курс на обучающей платформе онлайн-университета Skillbox и приступайте к обучению  
> [https://go.skillbox.ru/profession/profession-python/python-advanced/67a0dba9-8a72-4c9f-b3cb-f63504082c9b/longread](https://go.skillbox.ru/profession/profession-python/python-advanced/67a0dba9-8a72-4c9f-b3cb-f63504082c9b/longread)  
**Distinguishing test iterations using subtests:**

> [!info] unittest — Unit testing framework  
> Source code: Lib/unittest/__init__.  
> [https://docs.python.org/3/library/unittest.html#distinguishing-test-iterations-using-subtests](https://docs.python.org/3/library/unittest.html#distinguishing-test-iterations-using-subtests)  
## Sample Code
### Testing Flask App
```Python
import unittest
from datetime import datetime
from freezegun import freeze_time
from module_03_ci_culture_beginning.homework.hw1.hello_word_with_day import (
    GREETINGS,
    app,
)

class TestHelloWorldWithDayApp(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()
        self.base_url = "/hello-world/"
    def test_username_in_response(self):
        username = "Username"
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertIn(username, response_text)
    def test_weekday_in_response(self):
        username = "Username"
        # Create dates from monday (index = 0) to sunday (index = 6)
        datetimes = (datetime(2023, 10, day) for day in range(9, 16))
        # Test response for each weekday
        for weekday in range(0, 7):
            with freeze_time(datetimes):
                response = self.app.get(self.base_url + username)
                response_text = response.data.decode()
                self.assertIn(username, response_text)
                self.assertIn(GREETINGS[weekday], response_text)
```
### Using `self.subTest()`
```Python
import unittest
from module_03_ci_culture_beginning.homework.hw2.decrypt import decrypt

class TestDecryptFunction(unittest.TestCase):
    test_cases = (
        ("абра-кадабра.", "абра-кадабра"),
        ("абраа..-кадабра", "абра-кадабра"),
        ("абраа..-.кадабра", "абра-кадабра"),
        ("абра--..кадабра", "абра-кадабра"),
        ("абрау...-кадабра", "абра-кадабра"),
        ("абра........", ""),
        ("абр......a.", "a"),
        ("1..2.3", "23"),
        (".", ""),
        ("1.......................", ""),
    )
    def test_decrypt(self):
        for test_case in self.test_cases:
            encrypted, decrypted = test_case
            with self.subTest(encrypted=encrypted, decrypted=decrypted):
                self.assertEqual(decrypt(encrypted), decrypted)
```

----
📂 [[Unittests]] | Последнее изменение: 07.02.2024 20:16