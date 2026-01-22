
from main.tournament_winner import tournament_winner_with_out_points ,tournament_winner_with_points

def test_one():
    assert tournament_winner_with_out_points([["HTML","C#"],["C#","Python"],["Python","HTML"]],[0,0,1]) =="Python"
    assert tournament_winner_with_points([["HTML","C#"],["C#","Python"],["Python","HTML"]],[0,0,1]) =="Python"
    
    
def test_two():
    assert  tournament_winner_with_out_points([["HTML","Java"],["Java","Python"],["Python","HTML"]],[0,1,1])== 'Python'
    assert  tournament_winner_with_points([["HTML","Java"],["Java","Python"],["Python","HTML"]],[0,1,1])=='Python'


def test_three():
    assert tournament_winner_with_points([["HTML","Java"],["Java","Python"],["Python","HTML"],["C#","Python"],["Java","C#"],["C#","HTML"]],[0,1,1,1,0,1]) =='Python'
    assert tournament_winner_with_out_points([["HTML","Java"],["Java","Python"],["Python","HTML"],["C#","Python"],["Java","C#"],["C#","HTML"]],[0,1,1,1,0,1]) =='Python'


def test_four():
    assert tournament_winner_with_points([["HTML","Java"],["Java","Python"],["Python","HTML"],["C#","Python"],["Java","C#"],["C#","HTML"],["SQL","C#"],["HTML","SQL"],["SQL","Python"],["SQL","Java"]],[0,1,1,1,0,1,0,1,1,0]) =='Java'
    assert tournament_winner_with_out_points([["HTML","Java"],["Java","Python"],["Python","HTML"],["C#","Python"],["Java","C#"],["C#","HTML"],["SQL","C#"],["HTML","SQL"],["SQL","Python"],["SQL","Java"]],[0,1,1,1,0,1,0,1,1,0]) =='Java'

   
def test_five():
    assert tournament_winner_with_points([["Bulls","Eagles"]],[1]) == 'Bulls'
    assert tournament_winner_with_out_points([["Bulls","Eagles"]],[1]) =='Bulls'


def test_six():
    assert tournament_winner_with_points([["Bulls","Eagles"],["Bulls","Bears"],["Bears","Eagles"]],[0,0,0]) == 'Eagles'
    assert tournament_winner_with_out_points([["Bulls","Eagles"],["Bulls","Bears"],["Bears","Eagles"]],[0,0,0]) == 'Eagles'

def test_seven():
    assert tournament_winner_with_points([["Bulls","Eagles"],["Bulls","Bears"],["Bulls","Monkeys"],["Eagles","Bears"],["Eagles","Monkeys"],["Bears","Monkeys"]],[1,1,1,1,1,1]) =='Bears'
    assert tournament_winner_with_out_points([["Bulls","Eagles"],["Bulls","Bears"],["Bulls","Monkeys"],["Eagles","Bears"],["Eagles","Monkeys"],["Bears","Monkeys"]],[1,1,1,1,1,1]) == 'Bears'

def test_eight():
    assert tournament_winner_with_points([["AlgoMasters","FrontPage Freebirds"],["Runtime Terror","Static Startup"],["WeC#","Hypertext Assassins"],["AlgoMasters","WeC#"],["Static Startup","Hypertext Assassins"],["Runtime Terror","FrontPage Freebirds"],["AlgoMasters","Runtime Terror"],["Hypertext Assassins","FrontPage Freebirds"],["Static Startup","WeC#"],["AlgoMasters","Static Startup"],["FrontPage Freebirds","WeC#"],["Hypertext Assassins","Runtime Terror"],["AlgoMasters","Hypertext Assassins"],["WeC#","Runtime Terror"],["FrontPage Freebirds","Static Startup"]],[1,0,0,1,0,0,1,0,0,1,0,0,1,0,0]) =='Static Startup'
    assert tournament_winner_with_out_points([["AlgoMasters","FrontPage Freebirds"],["Runtime Terror","Static Startup"],["WeC#","Hypertext Assassins"],["AlgoMasters","WeC#"],["Static Startup","Hypertext Assassins"],["Runtime Terror","FrontPage Freebirds"],["AlgoMasters","Runtime Terror"],["Hypertext Assassins","FrontPage Freebirds"],["Static Startup","WeC#"],["AlgoMasters","Static Startup"],["FrontPage Freebirds","WeC#"],["Hypertext Assassins","Runtime Terror"],["AlgoMasters","Hypertext Assassins"],["WeC#","Runtime Terror"],["FrontPage Freebirds","Static Startup"]],[1,0,0,1,0,0,1,0,0,1,0,0,1,0,0]) == 'Static Startup'

def test_nine():
    assert tournament_winner_with_points([["HTML","Java"],["Java","Python"],["Python","HTML"],["C#","Python"],["Java","C#"],["C#","HTML"],["SQL","C#"],["HTML","SQL"],["SQL","Python"],["SQL","Java"]],[0,0,0,0,0,0,1,0,1,1]) =='SQL'
    assert tournament_winner_with_out_points([["HTML","Java"],["Java","Python"],["Python","HTML"],["C#","Python"],["Java","C#"],["C#","HTML"],["SQL","C#"],["HTML","SQL"],["SQL","Python"],["SQL","Java"]],[0,0,0,0,0,0,1,0,1,1]) =='SQL'

def test_ten():
    assert tournament_winner_with_out_points([["A","B"]],[0]) =='B'
    assert tournament_winner_with_points([["A","B"]],[0]) =='B'





