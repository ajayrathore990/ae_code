from main.best_digit import best_digit

def test_one():
    assert best_digit(2,"462839") =="4839"
    
def test_two():
    assert best_digit(4,"129847563")=="19876"
 
def test_three():
    assert best_digit(1,"19")=="1"
    
def test_four():
    assert best_digit(1,"22")=="2"
 
def test_five():
    assert best_digit(1,"23")=="2"
 
def test_six():
    assert best_digit(1,"123") =="13"
    
def test_seven():
    assert best_digit(1,"321") =="32"
 
def test_eight():
    assert best_digit(2,"123") =="1"
 
def test_nine():
    assert best_digit(2,"321") =="3"
 
def test_ten():
    assert best_digit(10,"11111111119999999999") == "1999999999"
 
def test_eleven():
    assert best_digit(9,"10000000002") == "12"

