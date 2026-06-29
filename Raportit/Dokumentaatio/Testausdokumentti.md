# Testausdokumentti

## 1. Yksikkötestaus
Ohjelman logiikka on testattu Pythonin pytest kirjastolla. Testit on keskitetty src/tests hakemistoon, ja ne testaavat sovelluksen algoritmeja ja tietorakenteita (src/model). Käyttöliittymä (Main.py) on eristetty testeistä kurssin vaatimusten mukaisesti, jotta testaus keskittyy puhtaasti laskennalliseen oikeellisuuteen.

### Testatut komponentit ja syötteiden edustavuus:
Testit on suunniteltu paitsi koodin toimivuuden, myös algoritmien oikeellisuuden todentamiseen erilaisilla syötteillä (yksinkertaiset toistot ja monimutkaisemmat syklit).

- FrequencyAnalysis: Testattu, että malli laskee siirtojen esiintyvyydet oikeasti ja palauttaa yleisimmän siirron. Syötteinä on käytetty sekä tasajakaumaa (ei selvää suosikkia) että selkeästi painotettua historiaa.
- MarkovChain: Testattu tilasiirtymämatriisin päivitystä. Syötteenä on käytetty ketjuja (esim. jatkuva Kivi -> Sakset -siirtymä), jotta nähdään ymmärtääkö malli peräkkäisyyden pelkän kokonaismäärän sijaan.
- PatternMatcher: Testattu kykyä tunnistaa toistuvia sarjoja. Testeissä on simuloitu "ihmismaistä" toistoa (esim. Kivi-Sakset-Paperi -sykli) ja varmistettu, että algoritmi löytää pisimmän mahdollisen vastineen historiasta.
- Sum: Testattu äänestysmekanismia ja painotuksien yhdistämistä. Testisyötteinä on käytetty tilanteita, joissa eri mallit antavat ristiriitaisia ennusteita, jotta nähdään valitseeko Sum-luokka painoarvoltaan vahvimman signaalin oikein.
- MarkovOrder: Testattu kertaluvun yleistäminen sekä get_move()- ja update_all()-rajapinta. Syötteinä on käytetty eri pituisia historioita (1–5 siirtoa) jotta varmistetaan, että tuple-avain rakentuu oikein, malli on satunnainen kun historia on lyhyempi kuin kertaluku, ja get_move() palauttaa oikean vastasiirron ennusteen perusteella.
- MultiMarkov: Testattu fokuspituus-valitsin sekä dominoivan mallin tunnistus. Testeissä on simuloitu useita kierroksia ja varmistettu, että pisteiden ikkuna F lasketaan oikein eikä koko historiaa.

### Testikattavuus
Testien haarautumakattavuus (branch coverage) on mitattu coverage-työkalulla.
- Branch coverage: 96% (274 koodiriviä, 22 testiä, vain 6 riviä puuttuu täydestä kattavuudesta).
- Testit ajetaan komennolla poetry run coverage run --branch -m pytest src/tests.

## 2. Manuaalinen testaus 
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

## 4. Multi-Markov pelin alussa (reunatapaus)**
- Toiminta: Pelataan 3–4 kierrosta heti pelin alusta — jolloin korkeiden kertalukujen malleilla ei ole vielä riittävästi historiaa
- Odotettu tulos: MultiMarkov palauttaa silti aina validin siirron (Kivi/Sakset/Paperi) eikä kaadu vaikka suurin osa malleista on satunnaisia
- Tulos: Toimi odotetusti, satunnainen valinta aktivoituu oikein

## 6. Syklialgoritmi (oppimisnopeuden testaus)**
- Toiminta: Syklialgoritmi pelaa Kivi→Sakset→Paperi toistuvasti
- Odotettu tulos: AI oppii kaavan nopeasti ja voittaa lähes jokaisen kierroksen
- Tulos: Molemmat AI:t voittivat 297/300 kierrosta (99%) — kaava opitaan muutamassa kierroksessa

## 7. Reaktioalgoritmi (ihmismäisen käyttäytymisen testaus)**
- Toiminta: Reaktioalgoritmi toistaa voittavan siirron ja vaihtaa satunnaisesti häviön jälkeen
- Odotettu tulos: Multi-Markov sopeutuu paremmin pitkässä pelissä koska se tunnistaa reaktiokaavan
- Tulos: 300 kierroksella molemmat pärjäävät tasaisesti (~+80). 10 000 kierroksella Multi-Markov selvästi parempi (+3992) kuin Äänestys-AI (+2872)

## 8. AI vs AI (peilimatsit)**
- Toiminta: Äänestys-AI ja Multi-Markov pelaavat toisiaan vastaan, molemmat päivittävät malliaan toisen siirroilla
- Odotettu tulos: Äänestys-AI vs Äänestys-AI tasan, Multi-Markov vs Multi-Markov lähes tasan
- Tulos: Äänestys-AI vs Äänestys-AI aina +0 . Multi-Markov voittaa Äänestys-AI:n konsistentisti (+722/+769 kierroksella 10 000) vaikka satunnaista pelaajaa vastaan Äänestys-AI näytti paremmalta. Multi-Markov vs Multi-Markov lähes nolla (+50/+61)

## 5. Dominoivan kertaluvun vaihtuminen**
- Toiminta: Pelataan ensin toistuvasti samaa siirtoa (esim. Kivi 10 kertaa), sitten vaihdetaan rytmi (Sakset–Paperi–Sakset–Paperi)
- Odotettu tulos: Dominoiva Markov-kertaluku vaihtuu pelin edetessä kun eri kertalukujen pärjääminen muuttuu
- Tulos: Dominoiva malli vaihtui ja loppuyhteenveto raportoi oikean kertaluvun

---

## 3. Suorituskykytestaus
Algoritmeille on tehty suorituskykytestejä mittaamalla päivitys- ja ennustusaikoja suurilla syötemäärillä. Tämä testaa ohjelman kykyä skaalautua pitkiin pelisessioihin, joissa historiaa on kertynyt paljon.

### Aikavaativuuden mittaus
Suorituskyky mitattiin erillisellä `performance.py` -skriptillä, joka simuloi tekoälyn toimintaa jatkuvalla syötteellä ilman käyttöliittymän hidasteita. Koska tietorakenteet on toteutettu tehokkaasti, aikavaativuus haku- ja päivitysoperaatioissa on O(1).

| Syötteen koko (iteraatioita) | Kokonaisaika (s) | Keskimääräinen aika / siirto (s) |
| :--- | :--- | :--- |
| 10 000 | 0.0210 | 0.000002 |

### Algoritmitestaus
Satunnainen testipelaaja korvattiin kahdella deterministisellä algoritmilla jotka jäljittelevät ihmiskäyttäytymistä paremmin. Syklialgoritmi pelaa aina Kivi→Sakset→Paperi-sarjaa — täysin ennustettava kaava jonka Markov-mallin pitäisi oppia muutamassa kierroksessa. Reaktioalgoritmi toistaa voittavan siirron ja vaihtaa satunnaisesti häviön jälkeen, mikä jäljittelee ihmispelaajan tyypillistä käyttäytymistä.

Lisäksi molemmat AI:t testattiin toisiaan vastaan. AI vs AI - tilanteessa kumpikin päivittää malliaan toisen oikeilla siirroilla.

Yksittäiset MarkovOrder-mallit (kertaluvut 1–5) testattiin myös samoja vastustajia vastaan. Tämä paljasti keskeisen löydöksen: **paras kertaluku riippuu vastustajan rakenteesta**. Satunnaista tai ihmisenkaltaista pelaajaa vastaan kertaluku 1 on paras (vähemmän tilaharvarautumista, enemmän dataa per tila). Strukturoituja AI-vastustajia vastaan kertaluvut 4–5 voittavat selvästi, koska ne tunnistavat pidempiä kaavoja. Tämä on juuri se syy miksi MultiMarkov on yksittäistä kertalukua parempi — se sopeutuu käyttämään oikeaa kertalukua riippumatta vastustajasta.

## Analyysi
Suorituskyky on erittäin hyvä. Yhden siirron laskeminen ja historian päivittäminen vie kaikilta kolmelta rinnakkaiselta mallilta erittäin vähän aikaa. Algoritmit toimivat reaaliajassa, eikä ohjelma hidastu merkittävästi edes 10 000 simuloidun kierroksen jälkeen. Muistinkäyttö ja aikavaativuus on saatu pidettyä optimaalisena hyödyntämällä sanakirjoja ja rajoittamalla kuvion tunnistuksen maksimisyvyyttä.

```text
Name                             Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------------------------
src/model/__init__.py                6      0      0      0   100%
src/model/markov.py                 13      0      4      0   100%
src/model/markov_kertaluku.py       28      0     10      0   100%
src/model/multi_markov.py           40      1     12      1    96%   33
src/model/pattern.py                20      1      8      1    93%   25
src/model/sum.py                    24      3     12      2    81%   20, 27-28
src/model/taajuus.py                 7      0      0      0   100%
src/tests/__init__.py                0      0      0      0   100%
src/tests/markov_test.py            12      0      0      0   100%
src/tests/multi_markov_test.py      77      1     14      1    98%   99
src/tests/pattern_test.py           14      0      2      0   100%
src/tests/sum_test.py               16      0      2      0   100%
src/tests/taajuus_test.py           12      0      0      0   100%
----------------------------------------------------------------------------
TOTAL                              269      6     64      5    96%
```
