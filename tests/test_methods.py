import unittest
import statistics as stat

from ark import Ark, ArkRow

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.r1 = ArkRow([1,2,3])
        self.r2 = ArkRow([3,2,1])
        self.r1r2 = ArkRow([4,4,4])

        self.ark = Ark([[1,2,3], [2,3,4],[3,4,5]], headers=['a', 'b', 'c'])
        self.col_sum = ArkRow([6, 9, 12])
        self.col_mean = ArkRow([2, 2, 2])

    def test_equal(self):
        self.assertEqual(self.r1, self.r1)
        

    def test_add(self):
        self.assertEqual(self.r1 + self.r2, self.r1r2)

    def test_sum(self):
        self.assertEqual(sum(self.ark), self.col_sum)

    def test_mean(self):
        self.assertEqual(stat.mean(self.ark), self.col_mean)
        
if __name__ == '__main__':
    unittest.main()
