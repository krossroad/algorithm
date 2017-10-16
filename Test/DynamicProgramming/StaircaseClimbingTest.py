import unittest

from DynamicProgramming.StaircaseClimbing import get_stair_cases_naive, get_stair_cases_dp


class TestGetStaircaseNaive(unittest.TestCase):
    def test_should_run(self):
        get_stair_cases_naive(0)

    def test_should_return_zero_for_n_zero(self):
        self.assertEquals(0, get_stair_cases_naive(0))

    def test_should_return_valid_possible_steps(self):
        self.assertEquals(1, get_stair_cases_naive(1))
        self.assertEquals(5, get_stair_cases_naive(4))
        self.assertEquals(8, get_stair_cases_naive(5))
        self.assertEquals(13, get_stair_cases_naive(6))


class TestGetStairCaseDp(unittest.TestCase):
    def test_should_run(self):
        get_stair_cases_dp(0)

    def test_should_return_zero_on_zero(self):
        self.assertEquals(0, get_stair_cases_dp(0))

    def test_should_return_valid_possible_steps(self):
        self.assertEquals(1, get_stair_cases_dp(1))
        self.assertEquals(2, get_stair_cases_dp(2))
        self.assertEquals(3, get_stair_cases_dp(3))
        self.assertEquals(5, get_stair_cases_dp(4))
        self.assertEquals(8, get_stair_cases_dp(5))
        self.assertEquals(13, get_stair_cases_dp(6))


if __name__ == '__main__':
    unittest.main()
