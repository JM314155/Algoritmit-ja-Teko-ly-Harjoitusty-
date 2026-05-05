class MarkovChain:
    def __init__(self):
        self.matrix = {
            'Kivi': {'Kivi': 0, 'Sakset': 0, 'Paperi': 0},
            'Sakset': {'Kivi': 0, 'Sakset': 0, 'Paperi': 0},
            'Paperi': {'Kivi': 0, 'Sakset': 0, 'Paperi': 0}
        }
        self.last_move = None


    def update(self, current_move):
        if self.last_move:
            self.matrix[self.last_move][current_move] += 1
        self.last_move = current_move

    def predict(self):
        if not self.last_move:
            return None
        
        predictions = self.matrix[self.last_move]
        return max(predictions, key=predictions.get)
