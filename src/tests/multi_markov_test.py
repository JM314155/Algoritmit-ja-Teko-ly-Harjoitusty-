import unittest
from model.markov_kertaluku import MarkovOrder
from model.multi_markov import MultiMarkov

class TestMarkovOrder(unittest.TestCase):

    def test_no_prediction_at_start(self):
        model = MarkovOrder(2)
        model.update('Kivi')
        self.assertIsNone(model.predict())

    def test_order1_learns_transition(self):
        model = MarkovOrder(1)
        model.update('Kivi')
        model.update('Sakset')
        model.update('Kivi')
        self.assertEqual(model.predict(), 'Sakset')

    def test_order2_uses_two_moves(self):
        model = MarkovOrder(2)
        for _ in range(3):
            model.update('Kivi')
            model.update('Paperi')
            model.update('Sakset')
        

        self.assertEqual(model.predict(), 'Kivi')

    def test_order3_requires_three_moves(self):
        model = MarkovOrder(3)
        model.update('Kivi')
        model.update('Sakset')
        
        model.update('Paperi')
        self.assertIsNone(model.predict())

    def test_order4_requires_four_moves(self):
        model = MarkovOrder(4)
        for s in ['Kivi', 'Sakset', 'Paperi']:
            model.update(s)
        self.assertIsNone(model.predict())

    def test_order5_random_at_start(self):
        model = MarkovOrder(5)
        for s in ['Kivi', 'Sakset', 'Paperi', 'Kivi']:
            model.update(s)
        self.assertIsNone(model.predict())


class TestMultiMarkov(unittest.TestCase):

    def test_returns_valid_move(self):
        ai = MultiMarkov(focus=5)
        move = ai.get_move()
        self.assertIn(move, ['Kivi', 'Sakset', 'Paperi'])

    def test_update_does_not_crash(self):
        ai = MultiMarkov(focus=5)
        for s in ['Kivi', 'Sakset', 'Paperi', 'Kivi', 'Sakset', 'Paperi']:
            ai.get_move()
            ai.update_all(s)

    def test_dominant_model_is_valid(self):
        ai = MultiMarkov(focus=5)
        for _ in range(10):
            ai.get_move()
            ai.update_all('Kivi')
        self.assertIn(ai.dominant_model(), [1, 2, 3, 4, 5])

    def test_focus_window_ignores_full_history(self):
        ai = MultiMarkov(focus=3)
        for s in ['Kivi'] * 10:
            ai.get_move()
            ai.update_all(s)
        self.assertIn(ai.get_move(), ['Kivi', 'Sakset', 'Paperi'])

    def test_five_models_exist(self):
        ai = MultiMarkov()
        self.assertEqual(len(ai.models), 5)
        self.assertEqual(ai.models[0].order, 1)
        self.assertEqual(ai.models[4].order, 5)


class TestMarkovOrderInterface(unittest.TestCase):

    def test_get_move_without_history_returns_valid(self):
        model = MarkovOrder(1)
        move = model.get_move()
        self.assertIn(move, ['Kivi', 'Sakset', 'Paperi'])

    def test_get_move_with_prediction_returns_counter(self):
        model = MarkovOrder(1)

        for _ in range(3):
            model.update('Kivi')
            model.update('Sakset')
        
        self.assertEqual(model.get_move(), 'Paperi')

    def test_update_all_grows_history(self):
        model = MarkovOrder(1)
        model.update_all('Kivi')

        model.update_all('Sakset')
        self.assertEqual(len(model.history), 2)


if __name__ == '__main__':
    unittest.main()
