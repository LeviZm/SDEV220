''' Module 5 - Programming Assignment - Testing
    This file contains unit tests
'''
import unittest
import my_sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        ''' Test that it can sum a list of integers'''
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result,6)

    def test_list_empty(self):
        data = []
        result = sum(data)
        self.assertEqual(result,0)
    
    def test_list_one_element(self):
        data = [5]
        result = sum(data)
        self.assertEqual(result,5)

if __name__ == "__main__":
    unittest.main()

