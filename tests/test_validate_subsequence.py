from main.validate_subsequence import correct_subsequence,correct_subsequence_

def test_one():
    assert correct_subsequence([5, 1, 22, 25, 6, -1, 8, 10],[1, 6, -1, 10])
    assert correct_subsequence_([5, 1, 22, 25, 6, -1, 8, 10],[1, 6, -1, 10])
    
def test_two():
    assert correct_subsequence([5,1,22,25,6,-1,8,10],[5,1,22,25,6,-1,8,10])
    assert correct_subsequence_([5,1,22,25,6,-1,8,10],[5,1,22,25,6,-1,8,10])

def test_three():
    assert correct_subsequence([5,1,22,25,6,-1,8,10],[5,1,22,6,-1,8,10])
    assert correct_subsequence_([5,1,22,25,6,-1,8,10],[5,1,22,6,-1,8,10])
    
def test_four():
    assert correct_subsequence([5,1,22,25,6,-1,8,10],[22,25,6])
    assert correct_subsequence_([5,1,22,25,6,-1,8,10],[22,25,6])

def test_five():
    assert correct_subsequence([5,1,22,25,6,-1,8,10],[1,6,10])
    assert correct_subsequence_([5,1,22,25,6,-1,8,10],[1,6,10])

def test_six():
    assert correct_subsequence([5,1,22,25,6,-1,8,10],[5,1,22,10])
    assert correct_subsequence_([5,1,22,25,6,-1,8,10],[5,1,22,10])
    
def test_seven():
    assert correct_subsequence([5,1,22,25,6,-1,8,10],[5,-1,8,10])
    assert correct_subsequence_([5,1,22,25,6,-1,8,10],[5,-1,8,10])

def test_eight():
    assert correct_subsequence([5,1,22,25,6,-1,8,10],[25])
    assert correct_subsequence_([5,1,22,25,6,-1,8,10],[25])

def test_nine():
    assert correct_subsequence([1,1,1,1,1],[1,1,1])
    assert correct_subsequence_([1,1,1,1,1],[1,1,1])

def test_ten():
    assert correct_subsequence([5,1,22,25,6,-1,8,10],[5,1,22,25,6,-1,8,10,12]) == False
    assert correct_subsequence_([5,1,22,25,6,-1,8,10],[5,1,22,25,6,-1,8,10,12]) == False

def test_eleven():
    assert correct_subsequence([5,1,22,25,6,-1,8,10],[5,1,22,23,6,-1,8,10]) == False
    assert correct_subsequence_([5,1,22,25,6,-1,8,10],[5,1,22,23,6,-1,8,10]) == False

