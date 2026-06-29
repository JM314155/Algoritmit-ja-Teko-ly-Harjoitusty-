import random
from model.markov_kertaluku import MarkovOrder

class MultiMarkov:
    def __init__(self, focus=5):
        self.focus = focus
        self.beats = {'Kivi': 'Paperi', 'Paperi': 'Sakset', 'Sakset': 'Kivi'}

        self.markov1 = MarkovOrder(1)
        self.markov2 = MarkovOrder(2)
        self.markov3 = MarkovOrder(3)
        self.markov4 = MarkovOrder(4)
        self.markov5 = MarkovOrder(5)
        self.models = [self.markov1, self.markov2, self.markov3, self.markov4, self.markov5]

        self.scores = [[] for _ in self.models]

    def get_move(self):
        best = self._select_best()
        prediction = self.models[best].predict()
        if not prediction:
            return random.choice(['Kivi', 'Sakset', 'Paperi'])
        return self.beats[prediction]

    def update_all(self, player_move):
        for i, model in enumerate(self.models):
            prediction = model.predict()
            if prediction is None:
                self.scores[i].append(0)
            elif prediction == player_move:
                self.scores[i].append(1)
            else:
                self.scores[i].append(-1)
            model.update(player_move)

    def _select_best(self):
        best_index = 0
        best_score = float('-inf')
        for i, scores in enumerate(self.scores):
            window = scores[-self.focus:] if len(scores) >= self.focus else scores
            total = sum(window)
            if total > best_score:
                best_score = total
                best_index = i
        return best_index

    def dominant_model(self):
        return self._select_best() + 1
