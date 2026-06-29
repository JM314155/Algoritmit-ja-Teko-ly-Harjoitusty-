from model.markov import MarkovChain
from model.taajuus import FrequencyAnalysis
from model.pattern import PatternMatcher
from model.sum import Sum
from model.multi_markov import MultiMarkov

def play():
    models = [MarkovChain(), FrequencyAnalysis(), PatternMatcher()]
    ai = Sum(models)
    multi = MultiMarkov(focus=5)

    beats = {'Kivi': 'Paperi', 'Paperi': 'Sakset', 'Sakset': 'Kivi'}

    sum_score = {'voitto': 0, 'häviö': 0, 'tasapeli': 0}
    multi_score = {'voitto': 0, 'häviö': 0, 'tasapeli': 0}

    print("Kivi-Sakset-Paperi peli")
    print("Komennot: Kivi, Sakset, Paperi, L lopettaa")

    while True:
        player = input("\nValintasi: ").strip().capitalize()

        if player == 'L':
            break

        if player not in ['Kivi', 'Sakset', 'Paperi']:
            print("Virheellinen valinta")
            continue

        sum_move = ai.get_move()
        multi_move = multi.get_move()

        print(f"Äänestys-AI: {sum_move}")
        print(f"Multi-Markov: {multi_move}")

        def game_result(player_move, ai_move):
            if player_move == ai_move:
                return 'tasapeli'
            elif beats[player_move] == ai_move:
                return 'häviö'
            return 'voitto'

        sum_result = game_result(player, sum_move)
        multi_result = game_result(player, multi_move)

        sum_score[sum_result] += 1
        multi_score[multi_result] += 1

        print(f"Äänestys-AI → {sum_result} | Multi-Markov → {multi_result}")

        ai.update_all(player)
        multi.update_all(player)

    print("\n=== Loppuyhteenveto ===")
    print(f"Äänestys-AI:  Voitot {sum_score['voitto']} | Häviöt {sum_score['häviö']} | Tasapelit {sum_score['tasapeli']}")
    print(f"Multi-Markov: Voitot {multi_score['voitto']} | Häviöt {multi_score['häviö']} | Tasapelit {multi_score['tasapeli']}")
    print(f"Dominoiva Markov-kertaluku: {multi.dominant_model()}")

if __name__ == "__main__":
    play()
