import unittest
from model.sum import Sum
from model.taajuus import FrequencyAnalysis
from model.markov import MarkovChain

class TestSum(unittest.TestCase):
    def setUp(self):
        self.models = [FrequencyAnalysis(), MarkovChain()]
        self.ai = Sum(self.models)


    def test_random_move_when_no_predictions(self):
        move = self.ai.get_move()
        self.assertIn(move, ['Kivi', 'Sakset', 'Paperi'])

    def test_votes_are_calculated_correctly(self):
        for _ in range(5):
            self.ai.update_all('Kivi')
        
       
        koneen_siirto = self.ai.get_move()
        self.assertEqual(koneen_siirto, 'Paperi')
