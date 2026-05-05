import unittest
from model.taajuus import FrequencyAnalysis

class TestFrequencyAnalysis(unittest.TestCase):
    def setUp(self):
        self.ai = FrequencyAnalysis()


    def test_predict_returns_most_common_move(self):
        self.ai.update('Kivi')
        self.ai.update('Kivi')
        self.ai.update('Sakset')
        self.assertEqual(self.ai.predict(), 'Kivi')

    def test_default_prediction_when_no_data(self):
        
        self.assertIn(self.ai.predict(), ['Kivi', 'Sakset', 'Paperi'])
