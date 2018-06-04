import unittest
from DynamicProgramming.LongestNonRepeatingSubstring import lnr_substring_optimized, lnr_substring_naive


class LongestNonRepeatingSubstringNaiveTest(unittest.TestCase):

    def test_should_run(self):
        lnr_substring_naive("")

    def test_should_return_zero_on_empty(self):
        self.assertEquals(0, lnr_substring_naive(""))

    def test_should_return_proper_value(self):
        self.assertEquals(1, lnr_substring_naive("a"))
        self.assertEquals(2, lnr_substring_naive("ab"))
        self.assertEquals(3, lnr_substring_naive("abc"))
        self.assertEquals(3, lnr_substring_naive("abcabcbb"))
        self.assertEquals(3, lnr_substring_naive("abcacbbb"))


class LongestNonRepeatingSubstringOptimizedTest(unittest.TestCase):

    def test_should_run(self):
        lnr_substring_optimized("")

    def test_should_return_zero_on_empty(self):
        self.assertEquals(0, lnr_substring_optimized(""))

    def test_should_return_proper_value(self):
        self.assertEquals(1, lnr_substring_optimized("a"))
        self.assertEquals(2, lnr_substring_optimized("ab"))
        self.assertEquals(3, lnr_substring_optimized("abc"))
        self.assertEquals(3, lnr_substring_optimized("abcabcbb"))
        self.assertEquals(3, lnr_substring_optimized("abcacbbb"))

if __name__ == '__main__':
    unittest.main()
