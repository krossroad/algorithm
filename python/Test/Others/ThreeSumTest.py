import unittest
def three_sum_slow(nums):
    result = set()
    input_size = len(nums)


    for i in range(input_size - 2):
        for j in range(i+1, input_size - 1):
            for k in range(j+1, input_size):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.add(
                        tuple(sorted([nums[i], nums[j], nums[k]]))
                    )

    return map(list, result)

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
