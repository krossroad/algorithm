import unittest

from DynamicProgramming.LongestPallindrome import get_longest_palindrome_dp, get_longest_palindrome_naive


class TestLongestPalindromeDP(unittest.TestCase):
    def test_should_return_empty_on_empty(self):
        self.assertEquals("", get_longest_palindrome_dp())


class TestLongestPalindromeNaive(unittest.TestCase):
    def test_should_return_empty_on_empty(self):
        self.assertEquals("", get_longest_palindrome_naive(""))

    def test_should_return_empty_on_non_palindrome(self):
        self.assertEquals("", get_longest_palindrome_naive("adfladjflakdjfladkfj"))
        self.assertEquals("", get_longest_palindrome_naive("abca"))

    def test_should_return_self_in_palindrome(self):
        self.assertEquals("aa", get_longest_palindrome_naive("aa"))
        self.assertEquals("aaa", get_longest_palindrome_naive("aaa"))

    def test_should_return_longest_palindrome_in_mixed(self):
        self.assertEquals("aa", get_longest_palindrome_naive("aab"))
        self.assertEquals("aa", get_longest_palindrome_naive("baa"))
        self.assertEquals("ababacababa", get_longest_palindrome_naive("ababacababa"))
        self.assertEquals("abcba", get_longest_palindrome_naive("abcbade"))
        self.assertEquals("aaaaa", get_longest_palindrome_naive("axadfadfaaaaalkdfafad"))