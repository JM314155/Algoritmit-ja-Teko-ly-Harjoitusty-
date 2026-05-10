# Algoritmit-ja-Teko-ly-Harjoitustyö-
Kivi-Sakset-Paperi
## ALGO, Tietojenkäsittelytieteen kandidaatti (TKT), Suomi

Tämä on Aineopintojen harjoitustyö: Algoritmit ja tekoäly harjoitustyö, jossa on toteutettu Kivi-Sakset-Paperi peliä pelaava tekoäly. Tekoäly analysoi pelaajan aiemmat siirrot ja pyrkii oppimaan niistä käyttämällä taajuusanalyysiä, Markovin ketjuja sekä kuvioiden tunnistusta (Pattern Matching).

Tekoäly hyödyntää useita rinnakkaisia algoritmeja:
## Taajuusanalyysi: Laskee pelaajan yleisimmät siirrot.
* Algoritmi seuraa kunkin siirron esiintymiskertoja pelihistorian ajalta ja ennustaa seuraavaksi siirroksi pelaajan tilastollisesti suosituimman valinnan.

**Kaava:**
```math
\hat{i}_{t+1} = \arg\max_{i \in \{K, S, P\}} \text{count}(i)
```
* $i$: Siirto (Kivi, Sakset tai Paperi).
* $\text{count}(i)$: siirron kokonaismäärä historiassa.

## Markovin ketjut: Ennustaa seuraavan siirron edellisten siirtojen perusteella.
Ensimmäisen kertaluvun Markovin ketju ennustaa seuraavan siirron nykyisen siirron perusteella, Se laskee siirtymätodennäköisyyksiä tilasta $S_t$ seuraavaan tilaan.

**Kaava:**
```math
\hat{S}_{t+1} = \arg\max_{i} \text{count}(S_t \to i)
```

* $S_t$: Pelaajan viimeisin siirto (nykyinen tila).
* $S_t \to i$: Siirtymien määrä nykyisestä siirrosta siirtoon $i$.
  
##Kuvioiden tunnistus (Pattern Matching): Etsii historiasta toistuvia syklejä.
Algoritmi etsii historiasta tietyn pituista sarjaa ($N$) ja tarkistaa mikä siirto on useimmiten seurannut tätä kyseistä sarjaa aiemmin.

**Kaava:**
```math
\hat{i}_{t+1} = \arg\max_{i} \text{count}((i_{t-N}, \dots, i_t) \to i)
```
* $(i_{t-N}, \dots, i_t)$: $N$:n pituinen siirtohistoria (kuvio).
* $\text{depth}$: Historian pituus, jota algoritmi tarkastelee.
  
## Summamenetelmä: Tekee lopullisen päätöksen yhdistämällä eri algoritmien tulokset.

**Ennusteen valinta:**
```math 
$$\hat{I}_{pelaaja} = \arg\max_{i} \sum_{k=1}^{n} [P_k = i]
```

**Lopullinen vastasiirto:**
```math
\text{Tekoälyn siirto} = \text{beat}(\hat{I}_{pelaaja})$$
```
* $P_k$: Mallin $k$ antama ennuste.
* $[P_k = i]$: Indikaattorifunktio (1 jos mallin ennuste on $i$, muuten 0).
  
## Dokumentaatio

Kaikki projektin dokumentit löytyvät kansiosta `Raportit/`:
* [Määrittelydokumentti](Raportit/Dokumentaatio/Määrittelydokumentti.md)
* [Toteutusdokumentti](Raportit/Dokumentaatio/Toteutusdokumentti.md)
* [Testausdokumentti](Raportit/Dokumentaatio/Testausdokumentti.md)
* [Viikkoraportit](Raportit/Viikkoraportit/)

## Asennus ja käynnistys


## 1 Asenna riippuvuudet:
   - poetry install

## 2 Käynnistä peli:
- poetry run python3 src/Main.py

Peliä pelataan komentoriviltä kirjoittamalla **Kivi**, **Sakset** tai **Paperi**. Pelin voi lopettaa syöttämällä **L**.

## Testaus

Projektin testit on toteutettu pytest kirjastolla.

## Yksikkötestien ajaminen
### Aja kaikki testit komennolla:
- export PYTHONPATH=$PYTHONPATH:$(pwd)/src
- poetry run pytest src/tests

## Testikattavuus
Testikattavuusraportin saa ajamalla:
- poetry run coverage run --branch -m pytest src/tests
- poetry run coverage report -m

## Suorituskykytestaus
### aja suorituskykytesti (10 000 simuloitua kierrosta):
- poetry run python3 src/performance.py
