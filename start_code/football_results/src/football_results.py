

def get_result(score):
    home_score = score["home_score"]
    away_score = score["away_score"]
    if home_score > away_score:
        return "home win"
    elif home_score < away_score:
        return "away win"
    elif home_score == away_score:
        return "draw"

def get_results(final_scores):
    pass
    # (You could try and use a list comprehension for this)