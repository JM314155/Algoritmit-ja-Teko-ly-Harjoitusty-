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
  
## Laajennus: Markovin ketjujen kertaluvut ja Multi-Markov
Projekti laajentaa alkuperäistä Markov-mallia tukemaan useita kertalukuja sekä dynaamista mallinvalintaa Wang et al. (2020) tutkimuksen pohjalta.

## Kertaluvun yleistys (MarkovOrder): Muistaa N edellistä siirtoa yhden sijaan.
* Alkuperäinen Markov-malli käyttää tilana yhtä edellistä siirtoa. Laajennetussa versiossa tila on N:n pituinen tuple edellisistä siirroista, jolloin kertaluku on vapaasti valittavissa.

**Kaava:**

```math
\hat{S}_{t+1} = \arg\max_{i} \text{count}((S_{t-N+1}, \dots, S_t) \to i)
```
* $N$: Kertaluku — kuinka monta edellistä siirtoa muodostaa tilan.
* $(S_{t-N+1}, \dots, S_t)$: N:n pituinen siirtohistoria (tuple-avain sanakirjassa).
* $S_t \to i$: Siirtymien määrä tästä tilasta siirtoon $i$.

| Kertaluku | Muistaa | Mahdolliset tilat |
|---|---|---|
| 1 | 1 siirron | 3 |
| 2 | 2 siirtoa | 9 |
| 3 | 3 siirtoa | 27 |
| 5 | 5 siirtoa | 243 |

## Multi-Markov ja fokuspituus: Valitsee parhaan kertaluvun dynaamisesti.
* Multi-Markov pitää viisi Markov-mallia (kertaluvut 1–5) käynnissä samanaikaisesti. Fokuspituus F määrää kuinka monen viimeisen kierroksen perusteella paras malli valitaan ennustamaan seuraava siirto.

**Mallinvalintakaava:**

```math
k^* = \arg\max_{k \in \{1,\dots,5\}} \sum_{j=t-F+1}^{t} \mathbf{1}[P_k^{(j)} = i_j]
```

**Lopullinen vastasiirto:**

```math
\text{Tekoälyn siirto} = \text{beat}(\hat{S}_{k^*})
```
* $F$: Fokuspituus — kuinka monen kierroksen ikkuna pisteytykseen käytetään.
* $k^*$: Parhaiten pisteytetty malli ikkunassa $F$.
* $\mathbf{1}[P_k^{(j)} = i_j]$: Indikaattorifunktio — 1 jos malli $k$ ennusti oikein kierroksella $j$, muuten 0.

## Summamenetelmä vs. Multi-Markov: Kaksi rinnakkaista arkkitehtuuria.
* Alkuperäinen Sum-luokka kerää kaikkien mallien ennusteet ja äänestää. Multi-Markov sen sijaan valitsee joka kierros yhden parhaan mallin ja antaa sille yksinoikeuden ennustaa.

| | Äänestys (Sum) | Multi-Markov |
|---|---|---|
| Mallit | Markov + Pattern + Taajuus | Markov kertaluvut 1–5 |
| Päätös | Kaikki äänestävät yhtä aikaa | Yksi paras kerrallaan |
| Sopeutuminen | Kiinteä rakenne | Vaihtuu F kierroksen välein |

Lähde: Wang, L. et al. (2020). Multi-AI competing and winning against humans in iterated Rock-Paper-Scissors game. Scientific Reports, 10, 13873.

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
- poetry run python3 src/main.py

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
### aja suorituskykytesti:
- poetry run python3 src/performance.py

Ajaa automaattisesti seuraavat testit:
1. Ajoaikatesti (10 000 kierrosta) — mittaa nopeuden
2. Kertalukujen vertailu (300 kierrosta) — mallit yksin satunnaista pelaajaa vastaan
3. Kertalukujen vertailu (10 000 kierrosta) — sama enemmällä datalla
4. Fokuspituuden vertailu (F = 3, 5, 10, 20)
5. Äänestys vs. Multi-Markov (300 kierrosta)
6. Äänestys vs. Multi-Markov (10 000 kierrosta)
7. Bottitestaus (300 kierrosta) — molemmat AI:t neljää vastustajaa vastaan
8. Bottitestaus (10 000 kierrosta) — sama enemmällä datalla

Vastustajatestauksessa vastustajina:
* **Syklialgoritmi** — pelaa Kivi→Sakset→Paperi toistuvasti
* **Reaktioalgoritmi** — toistaa voittavan siirron, vaihtaa häviöllä
* **Äänestys-AI** — alkuperäinen Sum-pohjainen tekoäly
* **Multi-Markov** — dynaaminen kertaluku-valitsin
