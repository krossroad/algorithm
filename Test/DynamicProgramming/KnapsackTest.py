import unittest

from DynamicProgramming.Knapsack import knapsack_naive


class KnapsackNaiveTest(unittest.TestCase):
    def test_should_run(self):
        knapsack_naive([], [], 0)

    def test_should_return_zero_for_zero(self):
        self.assertEquals(0, knapsack_naive([], [], 0))

    def test_should_return_proper_value(self):
        self.assertEquals(1, knapsack_naive([1], [1], 1))
        self.assertEquals(1, knapsack_naive([1, 4], [1, 3], 2))
        self.assertEquals(5, knapsack_naive([1, 4, 5], [1, 3, 4], 4))
        self.assertEquals(9, knapsack_naive([1, 4, 5, 7], [1, 3, 4, 5], 7))


if __name__ == '__main__':
    unittest.main()
