import unittest

from DynamicProgramming.RodCutting import rod_cutting_naive, rod_cutting_dp


class RodCuttingDp(unittest.TestCase):
    def test_should_run(self):
        rod_cutting_dp([], [], 0)

    def test_should_return_zero_for_empty_values_and_zero_length(self):
        self.assertEquals(0, rod_cutting_dp([], [], 100))
        self.assertEquals(0, rod_cutting_dp([1, 3], [1, 23], 0))
        self.assertEquals(0, rod_cutting_dp([1, 3], [1, 23], -1))

    def test_should_expected_profit(self):
        self.assertEquals(1, rod_cutting_dp([1], [1], 1))
        self.assertEquals(10, rod_cutting_dp([1, 2, 3, 4, 5, 6, 7, 8], [1, 5, 8, 9, 10, 17, 17, 20], 4))


class RodCuttingNaive(unittest.TestCase):
    def test_should_run(self):
        rod_cutting_naive([], [], 100),

    def test_should_return_zero_for_empty(self):
        self.assertEquals(0, rod_cutting_naive([], [], 100))
        self.assertEquals(0, rod_cutting_naive([1], [2], 0))

    def test_return_expected_profit(self):
        self.assertEquals(1, rod_cutting_naive([1], [1], 1))
        self.assertEquals(10, rod_cutting_naive([1, 2, 3, 4, 5, 6, 7, 8], [1, 5, 8, 9, 10, 17, 17, 20], 4))


if __name__ == '__main__':
    unittest.main()
