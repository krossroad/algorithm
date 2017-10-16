import unittest

from DynamicProgramming.SubsetSum import subset_sum_naive, subset_sum_dp


class SubsetSumNaiveTest(unittest.TestCase):
    def test_should_run(self):
        subset_sum_naive([], 0, 3, 0)

    def test_should_return_true_for_zero(self):
        self.assertEquals(True, subset_sum_naive([], 0, 0, 0))
        self.assertEquals(True, subset_sum_naive([1, 2, 3, 4], 0, 3, 0))

    def test_should_return_correct_judgement(self):
        self.assertEquals(True, subset_sum_naive([1, 2], 0, 2, 3))
        self.assertEquals(False, subset_sum_naive([5, 7], 0, 2, 3))
        self.assertEquals(True, subset_sum_naive([2, 3, 7, 8, 9], 0, 5, 11))


class SubsetSumDpTest(unittest.TestCase):
    def test_should_run(self):
        subset_sum_dp([], 0)

    def test_should_be_true_zero_sum(self):
        self.assertEquals(True, subset_sum_dp([], 0))
        self.assertEquals(True, subset_sum_dp([1, 2, 3, 4], 0))

    def test_should_return_correct_judgement(self):
        self.assertTrue(subset_sum_dp([1, 2], 3))
        self.assertFalse(subset_sum_dp([5, 7], 3))
        self.assertTrue(subset_sum_dp([2, 3, 7, 8, 9], 11))


if __name__ == '__main__':
    unittest.main()
