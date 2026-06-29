import time
import random
from src.model.markov import MarkovChain
from src.model.taajuus import FrequencyAnalysis
from src.model.pattern import PatternMatcher
from src.model.sum import Sum
from src.model.markov_kertaluku import MarkovOrder
from src.model.multi_markov import MultiMarkov

def run_performance_test(rounds=10000):
    models = [MarkovChain(), FrequencyAnalysis(), PatternMatcher()]
    ai = Sum(models)

    print(f"Suoritetaan {rounds} simuloitua kierrosta")
    start = time.time()
    for _ in range(rounds):
        ai.get_move()
        ai.update_all("Kivi")
    end = time.time()

    total_time = end - start
    print("-" * 30)
    print(f"Kokonaisaika:    {total_time:.4f} sekuntia")
    print(f"Aika per siirto: {total_time/rounds:.6f} sekuntia")
    print("-" * 30)

def compare_orders(rounds=300):
    print(f"\n=== Kertalukujen vertailu ({rounds} kierrosta, satunnainen pelaaja: Kivi 40%, Sakset 30%, Paperi 30%) ===")
    moves = ['Kivi', 'Sakset', 'Paperi']
    beats = {'Kivi': 'Paperi', 'Paperi': 'Sakset', 'Sakset': 'Kivi'}

    player = random.choices(moves, weights=[0.4, 0.3, 0.3], k=rounds)

    originals = [
        ("Taajuusanalyysi", FrequencyAnalysis()),
        ("PatternMatcher ", PatternMatcher()),
        ("MarkovChain    ", MarkovChain()),
    ]
    for name, model in originals:
        score = 0
        for move in player:
            prediction = model.predict()
            if prediction:
                ai_move = beats[prediction]
                if beats[move] == ai_move:
                    score += 1
                elif beats[ai_move] == move:
                    score -= 1
            model.update(move)
        print(f"  {name}: {score:+d} pistettä")

    print()
    for k in range(1, 6):
        model = MarkovOrder(k)
        score = 0
        for move in player:
            prediction = model.predict()
            if prediction:
                ai_move = beats[prediction]
                if beats[move] == ai_move:
                    score += 1
                elif beats[ai_move] == move:
                    score -= 1
            model.update(move)
        print(f"  Markov kertaluku {k}: {score:+d} pistettä")

def compare_focus_lengths(rounds=300):
    print(f"\n=== Fokuspituus-vertailu ({rounds} kierrosta, satunnainen pelaaja: Kivi 40%, Sakset 30%, Paperi 30%) ===")
    moves = ['Kivi', 'Sakset', 'Paperi']
    beats = {'Kivi': 'Paperi', 'Paperi': 'Sakset', 'Sakset': 'Kivi'}
    player = random.choices(moves, weights=[0.4, 0.3, 0.3], k=rounds)

    for f in [3, 5, 10, 20]:
        ai = MultiMarkov(focus=f)
        score = 0
        for move in player:
            ai_move = ai.get_move()
            if beats[move] == ai_move:
                score += 1
            elif beats[ai_move] == move:
                score -= 1
            ai.update_all(move)
        print(f"  Fokus F={f:2d}: {score:+d} pistettä")

def compare_architectures(rounds=300):
    print(f"\n=== Äänestys vs. Multi-Markov ({rounds} kierrosta, satunnainen pelaaja: Kivi 40%, Sakset 30%, Paperi 30%) ===")
    moves = ['Kivi', 'Sakset', 'Paperi']
    beats = {'Kivi': 'Paperi', 'Paperi': 'Sakset', 'Sakset': 'Kivi'}
    player = random.choices(moves, weights=[0.4, 0.3, 0.3], k=rounds)

    sum_ai = Sum([MarkovChain(), FrequencyAnalysis(), PatternMatcher()])
    multi_ai = MultiMarkov(focus=5)

    sum_score = 0
    multi_score = 0

    for move in player:
        s = sum_ai.get_move()
        m = multi_ai.get_move()

        if beats[move] == s:
            sum_score += 1
        elif beats[s] == move:
            sum_score -= 1

        if beats[move] == m:
            multi_score += 1
        elif beats[m] == move:
            multi_score -= 1

        sum_ai.update_all(move)
        multi_ai.update_all(move)

    print(f"  Äänestys-AI:  {sum_score:+d} pistettä")
    print(f"  Multi-Markov: {multi_score:+d} pistettä")
    print(f"  Dominoiva kertaluku lopussa: {multi_ai.dominant_model()}")

def compare_bots(rounds=300):
    print(f"\n=== Bottitestaus ({rounds} kierrosta) ===")
    beats = {'Kivi': 'Paperi', 'Paperi': 'Sakset', 'Sakset': 'Kivi'}
    moves = ['Kivi', 'Sakset', 'Paperi']

    def make_players():
        return [
            ("Äänestys-AI ", Sum([MarkovChain(), FrequencyAnalysis(), PatternMatcher()])),
            ("Multi-Markov", MultiMarkov(focus=5)),
            ("Markov k=1  ", MarkovOrder(1)),
            ("Markov k=2  ", MarkovOrder(2)),
            ("Markov k=3  ", MarkovOrder(3)),
            ("Markov k=4  ", MarkovOrder(4)),
            ("Markov k=5  ", MarkovOrder(5)),
        ]

    def round_result(player_move, opponent_move):
        if beats[opponent_move] == player_move:
            return 1
        elif beats[player_move] == opponent_move:
            return -1
        return 0

    print("\n  vs Syklialgoritmi (Kivi→Sakset→Paperi→...):")
    for name, ai in make_players():
        score = 0
        for i in range(rounds):
            bot_move = moves[i % 3]
            ai_move = ai.get_move()
            score += round_result(ai_move, bot_move)
            ai.update_all(bot_move)
        print(f"    {name}: {score:+d} pistettä")

    print("\n  vs Reaktioalgoritmi (toistaa voiton, vaihtaa häviöllä):")
    for name, ai in make_players():
        score = 0
        bot_move = random.choice(moves)
        for _ in range(rounds):
            ai_move = ai.get_move()
            result = round_result(ai_move, bot_move)
            score += result
            ai.update_all(bot_move)
            if result == 1:
                bot_move = random.choice([m for m in moves if m != bot_move])
        print(f"    {name}: {score:+d} pistettä")

    print("\n  vs Äänestys-AI:")
    for name, ai in make_players():
        opponent = Sum([MarkovChain(), FrequencyAnalysis(), PatternMatcher()])
        score = 0
        for _ in range(rounds):
            ai_move = ai.get_move()
            opponent_move = opponent.get_move()
            score += round_result(ai_move, opponent_move)
            ai.update_all(opponent_move)
            opponent.update_all(ai_move)
        print(f"    {name}: {score:+d} pistettä")

    print("\n  vs Multi-Markov:")
    for name, ai in make_players():
        opponent = MultiMarkov(focus=5)
        score = 0
        for _ in range(rounds):
            ai_move = ai.get_move()
            opponent_move = opponent.get_move()
            score += round_result(ai_move, opponent_move)
            ai.update_all(opponent_move)
            opponent.update_all(ai_move)
        print(f"    {name}: {score:+d} pistettä")

if __name__ == "__main__":
    run_performance_test()
    compare_orders(rounds=300)
    compare_orders(rounds=10000)
    compare_focus_lengths()
    compare_architectures(rounds=300)
    compare_architectures(rounds=10000)
    compare_bots(rounds=300)
    compare_bots(rounds=10000)
