
from main.two_number_sum import number_sum_two ,number_sum_two_

def test_one():
    assert  number_sum_two([3, -4, 8, 11, 1, -1, 6], 10) == [11,-1]
    assert  number_sum_two_([3, -4, 8, 11, 1, -1, 6], 10) == [11,-1]
    
def test_two():
    assert  number_sum_two([4, 6], 10) == [4,6]
    assert  number_sum_two_([4, 6], 10) == [4,6]

def test_three():
    assert  number_sum_two([4, 6 ,1 ], 5) == [4,1]
    assert  number_sum_two_([4, 6, 1], 5) == [4,1]


def test_four():
    assert  number_sum_two([4, 6 ,1 ,-3], 3) == [6,-3]
    assert  number_sum_two_([4, 6, 1,-3], 3) == [6,-3]
    
def test_five():
    assert  number_sum_two([1,2,3,4,5,6,7,8,9], 17) == [8,9]
    assert  number_sum_two_([1,2,3,4,5,6,7,8,9], 17) == [8,9]

def test_six():
    assert  number_sum_two([1,2,3,4,5,6,7,8,9,15], 18) == [3,15]
    assert  number_sum_two_([1,2,3,4,5,6,7,8,9,15], 18) == [3,15]


def test_seven():
    assert  number_sum_two([-7,-5,-3,-1,0,1,3,5,7], -5) == [-5,0]
    assert  number_sum_two_([-7,-5,-3,-1,0,1,3,5,7], -5) == [-5,0]

def test_eight():
    assert  number_sum_two([-21,301,12,4,65,56,210,356,9,-47], 163) == [210,-47]
    assert  number_sum_two_([-21,301,12,4,65,56,210,356,9,-47], 163) == [210,-47]

def test_nine():
    assert  number_sum_two([-21,301,12,4,65,56,210,356,9,-47], 164) == []
    assert  number_sum_two_([-21,301,12,4,65,56,210,356,9,-47], 164) == []

def test_ten():
    assert  number_sum_two([3,5,-4,8,11,1,-1,6], 15) == []
    assert  number_sum_two_([3,5,-4,8,11,1,-1,6], 15) == []



