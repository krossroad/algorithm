import unittest


def knapsack_naive(values, weights, W):
    if W <= 0 or len(values) == 0 or len(weights) == 0:
        return 0

    value = values[0]
    weight = weights[0]
    values = values[1:]
    weights = weights[1:]

    print "W=%d, we=%d" % (W, weight)

    value_including = (value + knapsack_naive(values, weights, W - weight)) if W >= weight else 0
    value_excluding = knapsack_naive(values, weights, W)
    print "Value including=%d" % value_including
    print "Value excluding=%d" % value_excluding

    return max(value_including, value_excluding)


class KnapsackNaiveTest(unittest.TestCase):
    def test_should_run(self, args=None):
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
