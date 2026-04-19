class PatternMatcher:
    def __init__(self, depth=3):
        self.history = []
        self.patterns = {}
        self.depth = depth

    def update(self, move):
        self.history.append(move)
        if len(self.history) > self.depth:
            pattern = tuple(self.history[-(self.depth+1):-1])
            next_move = self.history[-1]
          
            if pattern not in self.patterns:
                self.patterns[pattern] = {'Kivi': 0, 'Sakset': 0, 'Paperi': 0}
            self.patterns[pattern][next_move] += 1

    def predict(self):
        if len(self.history) < self.depth:
            return None
        
        current_pattern = tuple(self.history[-self.depth:])
        if current_pattern in self.patterns:
            return max(self.patterns[current_pattern], key=self.patterns[current_pattern].get)
        return None
