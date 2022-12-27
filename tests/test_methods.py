import unittest

import ark

class TestMethods(unittest.TestCase):

    def test_equal(self):
        r1 = ArkRow([1,2,3])
        assert r1 == r1
        

    def test_sum(self):
        r1 = ArkRow([1,2,3])
        r2 = ArkRow([3,2,1])
        r1r2 = ArkRow([4,4,4])
        assert r1 + r2 == r1r2
        
