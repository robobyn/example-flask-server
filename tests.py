"""Unit tests for Python server routes.

assertEqual statements check results of route to ensure that the route is
returning only the expected data.

assertNotIn statements check results of route for server errors."""

from unittest import TestCase
from server import app
import datetime


class FlaskTestsRoutes(TestCase):
    """Flask tests that check server routes."""

    def setUp(self):
        """Set up test client before each test."""

        self.client = app.test_client()
        app.config["TESTING"] = True

    def test_hello(self):
        """Test /hello server route."""

        result = self.client.get("/hello?firstname=tien&lastname=nguyen&gender=m")

        self.assertEqual("Hello Mr Tien Nguyen", result.data)
        self.assertNotIn("Internal Server Error", result.data)

    def test_compute(self):
        """Test /compute server route."""

        result = self.client.get("/compute?num1=5&num2=3&operation=subtract")

        self.assertEqual("2.0", result.data)
        self.assertNotIn("Internal Server Error", result.data)

    def test_date(self):
        """Test /date route."""

        result = self.client.get("/date")

        # retrieve current date to compare to result of /date route
        correct_date = str(datetime.date.today())

        self.assertEqual(correct_date, result.data)
        self.assertNotIn("Internal Server Error", result.data)


if __name__ == "__main__":
    import unittest

    unittest.main()
