import unittest

from src.high_scores import latest, personal_best, personal_top_three, highest_to_lowest_sort

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.score = [999999, 12, 778, 696, 55, 90, 122]
        self.score2 = [5, 200, 66, 999, 999, 999]
        self.score3 = [1, 2]
        self.score4 = [1]

    def test_lastest_high_score(self):
        self.assertEqual(122, latest(self.score))
    # Tests
    
    def test_score_high_score(self):
        self.assertEqual(999999, personal_best(self.score))

    def test_top_3_high_scores(self):
        self.assertEqual([999999, 778, 696], personal_top_three(self.score))
    


    # Test ordered from highest to lowest
    def test_order_highest_to_lowest(self):
        self.assertEqual([999999, 778, 696, 122, 90, 55, 12], highest_to_lowest_sort(self.score))

    # Test top three when there is a tie
    def test_top_3_is_a_tie(self):
        self.assertEqual([999, 999, 999], personal_top_three(self.score2))


    # Test top three when there are less than three
    def test_when_less_than_3(self):
        self.assertEqual([2,1], personal_top_three(self.score3))

    # Test top three when there is only one
    
    def test_when_one(self):
        self.assertEqual([1],personal_top_three(self.score4))