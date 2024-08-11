## A standard for status in Python
Reference: https://www.b-list.org/weblog/2023/dec/04/python-http-status-codes/
```python
from http import HTTPStatus

from django.test import TestCase

class EndToEndTests(TestCase):
    """
    End-to-end tests of the application.

    """

    def test_home_page(self):
        """
        Test that the home page returns an HTTP "OK" response.

        """
        response = self.client.get("/")
        assert response.status_code == HTTPStatus.OK
```

----
📂 [[HTTP]]