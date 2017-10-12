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


def get_stair_cases_dp(n):
    if n <= 0:
        return 0
    elif n <= 1:
        return 1
    elif n <= 2:
        return 2

    previous = 1
    current = 2

    for i in xrange(3, n):
        next_val = previous + current
        previous = current
        current = next_val

    return previous + current


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


if __name__ == '__main__':
    unittest.main()
