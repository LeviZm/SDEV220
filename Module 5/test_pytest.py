''' Module 5 - Programming Assignment - Testing
    This file contains different unit tests
'''

import pytest
import my_sum

def test_sum_list():
    '''Test that it can sum a list of integers'''
    data = [1,2,3]
    assert sum(data) == 6

def test_list_empty():
    data = []
    assert sum(data) == 0

def test_list_one_element():
    data = [42]
    assert sum(data) == 42
