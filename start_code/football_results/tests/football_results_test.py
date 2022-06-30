import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    def setUp(self):
        self.score = {"home_score": 3,
                    "away_score": 1}
        self.score_2 = {"home_score": 1,
                    "away_score": 3}
        self.score_3 = {"home_score": 3,
                    "away_score": 3}


    def test_final_score_3_1_result_home_win(self):
        self.assertEqual("home win", get_result(self.score))

    def test_final_score_1_3_result_away_win(self):
        self.assertEqual("away win", get_result(self.score_2))

    def test_final_score_3_3_result_draw(self):
        self.assertEqual("draw", get_result(self.score_3))



if __name__ == "__main__":
    unittest.main()
