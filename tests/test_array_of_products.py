
from main.array_of_products import array_of_product,array_of_product_

def test_one():
    assert  array_of_product([5,1,4,2]) == [8, 40, 10, 20]
    assert  array_of_product_([5,1,4,2]) == [8, 40, 10, 20]
    
def test_two():
    assert  array_of_product([1,8,6,2,4]) == [384, 48, 64, 192, 96]
    assert  array_of_product_([1,8,6,2,4]) == [384, 48, 64, 192, 96]

def test_three():
    assert  array_of_product([-5,2,-4,14,-6]) == [672, -1680, 840, -240, 560]
    assert  array_of_product_([-5,2,-4,14,-6]) == [672, -1680, 840, -240, 560]


def test_four():
    assert  array_of_product([9,3,2,1,9,5,3,2]) == [1620, 4860, 7290, 14580, 1620, 2916, 4860, 7290]
    assert  array_of_product_([9,3,2,1,9,5,3,2]) == [1620, 4860, 7290, 14580, 1620, 2916, 4860, 7290]
    
def test_five():
    assert  array_of_product([4,4]) == [4,4]
    assert  array_of_product_([4,4]) == [4,4]

def test_six():
    assert  array_of_product([0,0,0,0]) == [0,0,0,0]
    assert  array_of_product_([0,0,0,0]) == [0,0,0,0]


def test_seven():
    assert  array_of_product([1,1,1,1]) == [1,1,1,1]
    assert  array_of_product_([1,1,1,1]) == [1,1,1,1]

def test_eight():
    assert  array_of_product([-1,-1,-1]) == [1,1,1]
    assert  array_of_product_([-1,-1,-1]) == [1,1,1]

def test_nine():
    assert  array_of_product([-1,-1,-1,-1]) == [-1,-1,-1,-1]
    assert  array_of_product_([-1,-1,-1,-1]) == [-1,-1,-1,-1]

def test_ten():
    assert  array_of_product([0,1,2,3,4,5,6,7,8,9]) == [362880,0,0,0,0,0,0,0,0,0]
    assert  array_of_product_([0,1,2,3,4,5,6,7,8,9]) == [0,0,0,0,0,0,0,0,0,0]



