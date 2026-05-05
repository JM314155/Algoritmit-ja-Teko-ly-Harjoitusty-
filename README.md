# Algoritmit-ja-Teko-ly-Harjoitustyö-
Kivi-Sakset-Paperi
## ALGO, Tietojenkäsittelytieteen kandidaatti (TKT), Suomi

Tämä on Aineopintojen harjoitustyö: Algoritmit ja tekoäly harjoitustyö, jossa on toteutettu Kivi-Sakset-Paperi peliä pelaava tekoäly. Tekoäly analysoi pelaajan aiemmat siirrot ja pyrkii oppimaan niistä käyttämällä taajuusanalyysiä, Markovin ketjuja sekä kuvioiden tunnistusta (Pattern Matching).

Tekoäly hyödyntää useita rinnakkaisia algoritmeja:
* Taajuusanalyysi: Laskee pelaajan yleisimmät siirrot.
* Markovin ketjut: Ennustaa seuraavan siirron edellisten siirtojen perusteella.
* Kuvioiden tunnistus (Pattern Matching): Etsii historiasta toistuvia syklejä.
* Summamenetelmä: Tekee lopullisen päätöksen yhdistämällä eri algoritmien tulokset.

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
