import unittest
from model.pattern import PatternMatcher

class TestPatternMatcher(unittest.TestCase):
    def setUp(self):
        self.ai = PatternMatcher(depth=3)

    def test_no_prediction_before_depth_reached(self):
        self.ai.update('Kivi')
        self.ai.update('Kivi')
        self.assertIsNone(self.ai.predict())


    def test_learns_repeating_pattern(self):
        moves = ['Kivi', 'Sakset', 'Paperi', 'Kivi', 'Sakset', 'Paperi', 'Kivi', 'Sakset']
        for m in moves:
            self.ai.update(m)
        
        self.assertEqual(self.ai.predict(), 'Paperi')
