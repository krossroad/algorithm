import unittest


def get_stair_cases_naive(n):
    if n <= 0:
        return 0
    elif n <= 1:
        return 1
    elif n <= 2:
        return 2

    return get_stair_cases_naive(n - 1) \
           + get_stair_cases_naive(n - 2)


class TestGetStairCaseNaive(unittest.TestCase):
    def test_should_run(self):
        get_stair_cases_naive(0)

    def test_should_return_zero_for_n_zero(self):
        self.assertEquals(0, get_stair_cases_naive(0))

    def test_should_return_valid_possible_steps(self):
        self.assertEquals(1, get_stair_cases_naive(1))
        self.assertEquals(5, get_stair_cases_naive(4))


if __name__ == '__main__':
    unittest.main()
