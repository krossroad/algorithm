import unittest

from DynamicProgramming.SubsetSum import array_partition_dp


class ArrayPartitionDp(unittest.TestCase):
    def test_should_run(self):
        array_partition_dp([])

    def test_should_return_false_for_empty(self):
        self.assertEquals(False, array_partition_dp([]))

    def test_should_give_correct_verdict(self):
        self.assertEquals(False, array_partition_dp([]))
        self.assertEquals(True, array_partition_dp([2, 1, 3, 4]))
        self.assertEquals(False, array_partition_dp([2, 1, 3, 5]))
        self.assertEquals(False, array_partition_dp([1, 1, 3]))


if __name__ == '__main__':
    unittest.main()
