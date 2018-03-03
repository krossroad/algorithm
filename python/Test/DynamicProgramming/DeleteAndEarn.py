import unittest

from DynamicProgramming.DeleteAndEarn import delete_and_run


class DeleteAndEarnTest(unittest.TestCase):
    def test_should_run(self):
        delete_and_run([])

    def test_should_return_correct_points(self):
        self.assertEquals(6, delete_and_run([3, 4, 2]))
        self.assertEquals(6, delete_and_run([3, 4, 2, 5, 5]))
        self.assertEquals(9, delete_and_run([2, 2, 3, 3, 3, 4]))
