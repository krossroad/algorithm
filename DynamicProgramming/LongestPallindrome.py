import unittest


def is_palindrome(tst_str, start=0, end=None):
    end = end if end else (len(tst_str) - 1)

    if end == start:
        return True

    return tst_str[start] == tst_str[end] and is_palindrome(tst_str, start + 1, end - 1)


def get_longest_palindrome_naive(plain_text):
    str_size = len(plain_text)

    if str_size < 2:
        return ""

    lp = ""
    lp_len = 0

    for j in range(0, str_size - 1):
        for i in range(j + 1, str_size):
            tst_str = ''.join(plain_text[j:i + 1])
            tst_str_len = (i - j)
            if is_palindrome(tst_str) and tst_str_len > lp_len:
                lp = tst_str
                lp_len = tst_str_len

    return lp


def get_longest_palindrome_dp():
    return ""


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


if __name__ == '__main__':
    unittest.main()
