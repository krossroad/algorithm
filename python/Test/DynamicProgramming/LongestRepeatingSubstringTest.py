import unittest
from DynamicProgramming.LongestRepeatingSubstring import longest_repeating_substring_dp


class LongestRepeatingSubstringDPTest(unittest.TestCase):

    def test_should_run(self):
        longest_repeating_substring_dp("")

    def test_should_return_zero_on_empty(self):
        self.assertEquals(0, longest_repeating_substring_dp(""))

    def test_should_proper_value(self):
        self.assertEquals(3, longest_repeating_substring_dp("AGTCAAGGTGGGAC"))
        self.assertEquals(3, longest_repeating_substring_dp("AABBBB"))


if __name__ == '__main__':
    unittest.main()
