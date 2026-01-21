from main.non_constructible_change import non_constructible_change

def test_one():
    assert  non_constructible_change([5,7,1,1,2,3,22]) == 20
      
def test_two():
     assert  non_constructible_change([1,1,1,1,1]) == 6

def test_three():
     assert  non_constructible_change([6,4,5,1,1,8,9]) == 3

def test_four():
     assert  non_constructible_change([]) == 1
    
def test_five():
     assert  non_constructible_change([87]) == 1
     
