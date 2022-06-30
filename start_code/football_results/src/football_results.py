

def get_result(score):
    if score["home_score"] > score["away_score"]:
        return "home win"
    elif score["home_score"] < score["away_score"]:
        return "away win"
    elif score["home_score"] == score["away_score"]:
        return "draw"

def get_list_of_scores(score, score2, score3):

    first_game = get_result(score)
    second_game = get_result(score2)
    third_game = get_result(score3)

    return [f'{first_game}, {second_game}, {third_game}']

