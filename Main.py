from model import MarkovChain, FrequencyAnalysis, PatternMatcher, Sum

def pelaa():
    mallit = [MarkovChain(), FrequencyAnalysis(), PatternMatcher()]
    
    ai = Sum(mallit)
    
    print("Kivi-Sakset-Paperi peli")
    print("Komennot: Kivi, Sakset, Paperi. 'L' lopettaa.")

    while True:
        pelaaja = input("\nValintasi: ").capitalize()
        
        if pelaaja == 'L':
            print("Peli päättyi.")
            break
            
        if pelaaja not in ['Kivi', 'Sakset', 'Paperi']:
            print("Virheellinen valinta")
            continue
        koneen_siirto = ai.get_move()
        
        print(f"AI: {koneen_siirto}")

        # 2. Tarkistetaan voittaja
        if pelaaja == koneen_siirto:
            print("Tasapeli")
        elif (pelaaja == "Kivi" and koneen_siirto == "Sakset") or \
             (pelaaja == "Sakset" and koneen_siirto == "Paperi") or \
             (pelaaja == "Paperi" and koneen_siirto == "Kivi"):
            print("Voitit kierroksen")
        else:
            print("AI voitti kierroksen")
        ai.update_all(pelaaja)

if __name__ == "__main__":
    pelaa()
