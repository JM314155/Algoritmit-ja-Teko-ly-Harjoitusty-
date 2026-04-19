from model import MarkovChain, FrequencyAnalysis, PatternMatcher, Sum

models = [MarkovChain(), FrequencyAnalysis(), PatternMatcher()]
ai = Sum(models)

print("Peli alkaa: Kirjoita Kivi, Sakset tai Paperi (tai lopeta, jos haluat lopettaa).")

while True:
    player = input("Pelaajan siirto: ").capitalize()
    if player == 'Lopeta': break
    
    computer_move = ai.get_move()
    print(f"AI valitsi: {computer_move}")
        
