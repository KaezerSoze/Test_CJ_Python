import unittest
from test import str_palindrome

class TestStrPalindrome(unittest.TestCase):

    def test_palindrome_simple(self):
        self.assertTrue(str_palindrome("radar"))

    def test_non_palindrome(self):
        self.assertFalse(str_palindrome("python"))

    def test_palindrome_espaces(self):
        self.assertTrue(str_palindrome("Panama"))

if __name__ == '__main__':
    unittest.main()
