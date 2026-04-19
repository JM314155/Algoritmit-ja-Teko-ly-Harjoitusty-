class FrequencyAnalysis:
    def __init__(self):
        self.counts = {'Kivi': 0, 'Sakset': 0, 'Paperi': 0}

    def update(self, move):
        self.counts[move] += 1

    def predict(self):
        return max(self.counts, key=self.counts.get)
