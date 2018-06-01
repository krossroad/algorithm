import unittest

from Others.ThreeSum import three_sum_faster, three_sum_slow

class ThreeSumSlowTest(unittest.TestCase):

    def test_should_be_able_to_run(self):
        three_sum_slow([])

    def test_should_return_empty_array_when_unable_to_find(self):
        self.assertEquals([], three_sum_slow([]))

    def test_should_return_result_when_matched(self):
        self.assertEquals([[-1, 0, 1]], three_sum_slow([1, 0, -1]))
        self.assertEquals([[-1, 0, 1]], three_sum_slow([1, 0, -1, 10]))
        self.assertEquals(
            [
                [-1, -1, 2],
                [-1, 0, 1]
            ],
            three_sum_slow([-1, 0, 1, 2, -1, -4])
        )


class ThreeSumFasterTest(unittest.TestCase):

    def test_should_be_able_to_run(self):
        three_sum_faster([])

    # def test_should_return_empty_array_when_unable_to_find(self):
    #     self.assertEquals([], three_sum_faster([]))

    def test_should_return_result_when_matched(self):
        self.assertEquals([[-1, 0, 1]], three_sum_faster([1, 0, -1]))
        self.assertEquals([[-1, 0, 1]], three_sum_faster([1, 0, -1, 10]))
        self.assertEquals(
            [
                [-1, -1, 2],
                [-1, 0, 1]
            ],
            three_sum_faster([-1, 0, 1, 2, -1, -4])
        )

if __name__ == '__main__':
    unittest.main()
