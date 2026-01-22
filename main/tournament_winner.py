"""
Category: Arrays
"""

def tournament_winner_with_out_points(matches,result):
    winners= []
    matches_result = zip(matches,result)
    for match in matches_result:
        if match[1]==0:
            winners.append(match[0][1])
        else:
            winners.append(match[0][0])
    return max(winners)


def tournament_winner_with_points(matches,results):
    home_team_won = 1
    current_best_team= ''
    scores = {current_best_team : 0}
    
    for index, match in enumerate(matches):
        result= results[index]
        home_team,away_team = match
        if result == home_team_won:
            winning_team =  home_team
        else:
            winning_team = away_team
    update_score(winning_team,3,scores)
    
    if scores[winning_team]> scores[current_best_team]:
        current_best_team =winning_team
        
    return current_best_team

def update_score(team,points,scores):
    if team not in scores:
        scores[team] = 0
    scores[team] = scores[team] + points


