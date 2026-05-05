import time
from src.model.markov import MarkovChain
from src.model.taajuus import FrequencyAnalysis
from src.model.pattern import PatternMatcher
from src.model.sum import Sum

def aja_suorituskykytesti(iteraatiot=10000):
    mallit = [MarkovChain(), FrequencyAnalysis(), PatternMatcher()]
    ai = Sum(mallit)
    
    
    print(f"Suoritetaan {iteraatiot} simuloitua kierrosta")
    alku = time.time()
    for _ in range(iteraatiot):
        ai.get_move()
        ai.update_all("Kivi")
    loppu = time.time()
    
    kokonaisaika = loppu - alku
    print("-" * 30)
    print(f"Kokonaisaika:    {kokonaisaika:.4f} sekuntia")
    print(f"Aika per siirto: {kokonaisaika/iteraatiot:.6f} sekuntia")
    print("-" * 30)


if __name__ == "__main__":
    aja_suorituskykytesti()
