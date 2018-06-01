import unittest

from DynamicProgramming.LongestCommonSubsequnce import calc_longest_common_sub_sequence_naive, \
    calc_longest_common_sub_sequence_dp


class LongestCommonSubSequenceNaiveTest(unittest.TestCase):
    def test_should_run(self):
        calc_longest_common_sub_sequence_naive("fool", "fool")

    def test_should_return_zero_empty_sequences(self):
        self.assertEquals(0, calc_longest_common_sub_sequence_naive("", "something random"))
        self.assertEquals(0, calc_longest_common_sub_sequence_naive("something random", ""))

    def test_should_return_correct_sub_sequence_length(self):
        self.assertEquals(4, calc_longest_common_sub_sequence_naive("ABAZDC", "BACBAD"))
        self.assertEquals(5, calc_longest_common_sub_sequence_naive("XYXZZYXZ", "XYZXXZ"))


class LongestCommonSubSequenceDpTest(unittest.TestCase):
    def test_should_run(self):
        calc_longest_common_sub_sequence_dp("fool", "fool")

    def test_should_return_zero_empty_sequences(self):
        self.assertEquals(0, calc_longest_common_sub_sequence_dp("", "some random"))
        self.assertEquals(0, calc_longest_common_sub_sequence_dp("some random", ""))

    def test_should_return_correct_sub_sequence_length(self):
        self.assertEquals(4, calc_longest_common_sub_sequence_dp("ABAZDC", "BACBAD"))

if __name__ == '__main__':
    unittest.main()
