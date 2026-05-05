# Testausdokumentti

## 1. Yksikkötestaus
Ohjelman logiikka on testattu Pythonin pytest kirjastolla. Testit on keskitetty src/tests hakemistoon, ja ne testaavat sovelluksen algoritmeja ja tietorakenteita (src/model). Käyttöliittymä (Main.py) on eristetty testeistä kurssin vaatimusten mukaisesti, jotta testaus keskittyy puhtaasti laskennalliseen oikeellisuuteen.

### Testatut komponentit ja syötteiden edustavuus:
Testit on suunniteltu paitsi koodin toimivuuden, myös algoritmien oikeellisuuden todentamiseen erilaisilla syötteillä (yksinkertaiset toistot ja monimutkaisemmat syklit).

- FrequencyAnalysis: Testattu, että malli laskee siirtojen esiintyvyydet oikeasti ja palauttaa yleisimmän siirron. Syötteinä on käytetty sekä tasajakaumaa (ei selvää suosikkia) että selkeästi painotettua historiaa.
- MarkovChain: Testattu tilasiirtymämatriisin päivitystä. Syötteenä on käytetty ketjuja (esim. jatkuva Kivi -> Sakset -siirtymä), jotta nähdään ymmärtääkö malli peräkkäisyyden pelkän kokonaismäärän sijaan.
- PatternMatcher: Testattu kykyä tunnistaa toistuvia sarjoja. Testeissä on simuloitu "ihmismaistä" toistoa (esim. Kivi-Sakset-Paperi -sykli) ja varmistettu, että algoritmi löytää pisimmän mahdollisen vastineen historiasta.
- Sum: Testattu äänestysmekanismia ja painotuksien yhdistämistä. Testisyötteinä on käytetty tilanteita, joissa eri mallit antavat ristiriitaisia ennusteita, jotta nähdään valitseeko Sum-luokka painoarvoltaan vahvimman signaalin oikein.

### Testikattavuus
Testien haarautumakattavuus (branch coverage) on mitattu coverage-työkalulla.
- Branch coverage**: 94% (122 koodiriviä, vain 4 riviä puuttuu täydestä kattavuudesta).
-Testit ajetaan komennolla poetry run coverage run --branch -m pytest src/tests.

## 2. Manuaalinen testaus (Käyttöliittymä ja Integraatio)
Kokonaisuuden toimivuus on varmistettu manuaalisesti pelaamalla tekoälyä vastaan suuria määriä kierroksia.

### Testitapaukset:

## 1. Yksinkertainen toisto (Taajuusanalyysin testaus)**
- Toiminta: Pelaaja syöttää "Kivi" useita kertoja putkeen
- Odotettu tulos: AI oppii, että pelaaja suosii kiveä, ja alkaa pelata jatkuvasti "Paperia"
- Tulos: Tekoäly mukautui ja vastasi oikein

## 2. Säännöllinen sarja (Markovin ketjun ja kuviontunnistuksen testaus)**
- Toiminta: Pelaaja syöttää toistuvasti monimutkaisempaa sarjaa
- Odotettu tulo: Tekoäly tunnistaa syklin nopeasti PatternMatcher ja Markov-mallien avulla ja lukitsee oikean vastasiirron jokaiseen vaiheeseen
- Tulos: Tekoäly oppi säännönmukaisuuden onnistuneesti

## 3. Virheellinen syöte ja reunatapaukset**
- Toiminta: Syötetään tyhjä merkkijono, väärä sana (esim. "Auto") tai lopetuskomento "L"
- Odotettu tulos: Ohjelma antaa virheilmoituksen, ei kaadu, ja ei tallenna virheellistä syötettä tekoälyn oppimishistoriaan
- Tulos: Virheenkäsittely toimi odotetusti

---

## 3. Suorituskykytestaus
Algoritmeille on tehty suorituskykytestejä mittaamalla päivitys- ja ennustusaikoja suurilla syötemäärillä. Tämä testaa ohjelman kykyä skaalautua pitkiin pelisessioihin, joissa historiaa on kertynyt paljon.

### Aikavaativuuden mittaus
Suorituskyky mitattiin erillisellä `performance.py` -skriptillä, joka simuloi tekoälyn toimintaa jatkuvalla syötteellä ilman käyttöliittymän hidasteita. Koska tietorakenteet on toteutettu tehokkaasti, aikavaativuus haku- ja päivitysoperaatioissa on O(1).

| Syötteen koko (iteraatioita) | Kokonaisaika (s) | Keskimääräinen aika / siirto (s) |
| :--- | :--- | :--- |
| 10 000 | 0.0210 | 0.000002 |

## Analyysi
Suorituskyky on erittäin hyvä. Yhden siirron laskeminen ja historian päivittäminen vie kaikilta kolmelta rinnakkaiselta mallilta erittäin vähän aikaa. Algoritmit toimivat reaaliajassa, eikä ohjelma hidastu merkittävästi edes 10 000 simuloidun kierroksen jälkeen. Muistinkäyttö ja aikavaativuus on saatu pidettyä optimaalisena hyödyntämällä sanakirjoja ja rajoittamalla kuvion tunnistuksen maksimisyvyyttä.

```text
Name                       Stmts   Miss Branch BrPart  Cover   Missing
-----------------------------------------------------------------------
src/model/__init__.py           4      0      0      0   100%
src/model/markov.py            13      0      4      0   100%
src/model/pattern.py           20      1      8      1    93%   24
src/model/sum.py               24      3     12      2    81%   19, 26-27
src/model/taajuus.py            7      0      0      0   100%
src/tests/__init__.py           0      0      0      0   100%
src/tests/markov_test.py       12      0      0      0   100%
src/tests/pattern_test.py      14      0      2      0   100%
src/tests/sum_test.py          16      0      2      0   100%
src/tests/taajuus_test.py      12      0      0      0   100%
-----------------------------------------------------------------------
TOTAL                         122      4     28      3    94% ```
