import unittest
from main_program import PalindromeChecker, OHCE

class TestStrPalindrome(unittest.TestCase):

    def test_palindrome_simple(self):
        self.assertTrue(PalindromeChecker.is_palindrome("Non"))

    def test_non_palindrome(self):
        self.assertFalse(PalindromeChecker.is_palindrome("python"))

    def test_palindrome_espaces(self):
        self.assertTrue(PalindromeChecker.is_palindrome("Bonjour"))

    def test_casse_palindrome(self):
        self.assertTrue(PalindromeChecker.is_palindrome("Epsi"))

if __name__ == '__main__':
    unittest.main()
