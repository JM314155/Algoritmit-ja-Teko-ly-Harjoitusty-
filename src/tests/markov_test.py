import unittest
from model.markov import MarkovChain

class TestMarkovChain(unittest.TestCase):
    def setUp(self):
        self.ai = MarkovChain()

    def test_no_prediction_on_first_turn(self):
        self.assertIsNone(self.ai.predict())



    def test_learns_simple_transition(self):
        self.ai.update('Kivi')
        self.ai.update('Sakset')
        self.ai.update('Kivi')
        
        self.assertEqual(self.ai.predict(), 'Sakset')
