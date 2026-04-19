import random

class Sum:
    def __init__(self, models):
        self.models = models
        self.wins = {model.__class__.__name__: 0 for model in models}
        self.last_predictions = {}
        self.beats = {'Kivi': 'Paperi', 'Paperi': 'Sakset', 'Sakset': 'Kivi'}

    def get_move(self):
        votes = {}
        for model in self.models:
            prediction = model.predict()
            if prediction:
                self.last_predictions[model.__class__.__name__] = prediction
                votes[prediction] = votes.get(prediction, 0) + 1
        
        if not votes:
            return random.choice(['Kivi', 'Sakset', 'Paperi'])
        
        predicted_player_move = max(votes, key=votes.get)
        return self.beats[predicted_player_move]

    def update_all(self, player_move):
        for name, pred in self.last_predictions.items():
            if pred == player_move:
                self.wins[name] += 1
        
        for model in self.models:
            model.update(player_move)
