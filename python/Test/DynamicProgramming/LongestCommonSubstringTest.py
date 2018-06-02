import unittest

from DynamicProgramming.LongestCommonSubstring import longest_common_substring_naive, longest_common_substring_dp


class LongestCommonSubstringNaiveTest(unittest.TestCase):

    def test_should_run(self):
        longest_common_substring_naive("", "")

    def test_should_return_zero_on_empty(self):
        self.assertEqual(0, longest_common_substring_naive("", ""))

    def test_should_return_valid_result(self):
        self.assertEqual(4, longest_common_substring_naive("ABABC", "BABCA"))
        self.assertEqual(2, longest_common_substring_naive("BAB", "ABC"))
        self.assertEqual(1, longest_common_substring_naive("BACB", "C"))


class LongestCommonSubstringDPTest(unittest.TestCase):

    def test_should_run(self):
        longest_common_substring_dp("", "")

    def test_should_return_zero_on_empty(self):
        self.assertEqual(0, longest_common_substring_dp("", ""))

    def test_should_return_valid_result(self):
        self.assertEqual(4, longest_common_substring_dp("ABABC", "BABCA"))
        self.assertEqual(2, longest_common_substring_dp("BAB", "ABC"))
        self.assertEqual(2, longest_common_substring_dp("BAB", "ABC"))
