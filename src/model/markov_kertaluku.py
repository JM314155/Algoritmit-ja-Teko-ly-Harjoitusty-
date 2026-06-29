import random

class MarkovOrder:
    beats = {'Kivi': 'Paperi', 'Paperi': 'Sakset', 'Sakset': 'Kivi'}

    def __init__(self, order=1):
        self.order = order
        self.transitions = {}
        self.history = []

    def update(self, move):
        if len(self.history) >= self.order:
            state = tuple(self.history[-self.order:])
            if state not in self.transitions:
                self.transitions[state] = {'Kivi': 0, 'Sakset': 0, 'Paperi': 0}
            self.transitions[state][move] += 1
        self.history.append(move)

    def predict(self):
        if len(self.history) < self.order:
            return None
        
        state = tuple(self.history[-self.order:])
        if state not in self.transitions:
            return None
        return max(self.transitions[state], key=self.transitions[state].get)

    def get_move(self):
        prediction = self.predict()
        if not prediction:
            return random.choice(['Kivi', 'Sakset', 'Paperi'])
        return self.beats[prediction]

    def update_all(self, move):
        self.update(move)
