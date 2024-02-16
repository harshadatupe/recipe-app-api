"""
Sample tests
"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 4)
        self.assertEqual(res, 9)

    def test_subtract_numbers(self):
        """Test subtracting numbers together."""
        res = calc.subtract(5, 4)
        self.assertEqual(res, 1)