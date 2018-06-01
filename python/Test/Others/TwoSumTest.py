import unittest

from Others.TwoSum import two_sum_naive

class TwoSumNaiveTest(unittest.TestCase):
    def test_should_run(self):
        two_sum_naive([], 0)

    def test_should_return_proper_value(self):
        self.assertEquals([0, 1], two_sum_naive([2, 7, 11, 15], 9))


if __name__ == '__main__':
    unittest.main()
