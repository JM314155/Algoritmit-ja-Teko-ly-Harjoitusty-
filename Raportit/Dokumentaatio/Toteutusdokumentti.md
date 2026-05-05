# Toteutusdokumentti
## Ohjelman yleisrakenne
Ohjelma on jaettu käyttöliittymästä huolehtivaan tiedostoon (Main.py) sekä tekoälyn logiikasta huolehtiviin luokkiin (src/model hakemisto). Tekoäly on jaettu itsenäisiin moduuleihin: MarkovChain, FrequencyAnalysis ja PatternMatcher. Pääluokka Sum toimii ensemblienä, joka kerää näiltä moduuleilta ennusteet sekö suorittaa äänestyksen ja päättää lopullisen siirron.
## Saavutetut aika- ja tilavaativuudet (esim. O-analyysit pseudokoodista)
Koska peli vaatii välitöntä reaktioaikaa ja siirtovaihtoehtoja on vain kolme, algoritmit on suunniteltu sanakirjojen avulla nopeiksi.

*   **Taajuusanalyysi (FrequencyAnalysis):**
    - Aikavaativuus: O(1) päivittämiseen ja ennustamiseen.
    - Tilavaativuus: O(1) (vain 3 avainta).
*   **Markovin ketju (MarkovChain):**
    - Aikavaativuus: O(1) sanakirjahaun ansiosta.
    - Tilavaativuus: O(1) (3x3 matriisi).
*   **Kuvioiden tunnistus (PatternMatcher):**
    - Aikavaativuus: O(D), missä D on haettavan kuvion syvyys (listan siivutus tuple(history[-depth:]) vie syvyyden verran operaatioita, mutta koska D on pieni vakio esim. 3, käytännössä O(1)).
    - Tilavaativuus: O(N) missä N on pelattujen kierrosten määrä (historia kasvaa).
*   **Sum-luokka:** Kutsuu moduuleja, joten aikavaativuus on O(1).

## Työn mahdolliset puutteet ja parannusehdotukset
Tällä hetkellä Sum luokka käyttää aika yksinkertaista enemmistöäänestystä, Vaikka ohjelma pitää kirjaa moduulien osumatarkkuudesta (self.wins), tätä dataa ei vielä aktiivisesti käytetä painottamaan parhaiten pärjäävän moduulin ääntä. Jatkossa algoritmi voisi antaa suuremman painoarvon sille tekoälylle, jolla on suurin osumaprosentti.
## Laajojen kielimallien (ChatGPT yms.) käyttö. Mainitse mitä mallia on käytetty ja miten. Mainitse myös mikäli et ole käyttänyt. Tämä on tärkeää!
Yliopiston Currechattia/GPT on käytetty koodin virheanalyysissa sekä koodin korjaamisessa sekä tiivistämisessä/siistimisessä/optimoinnissa
VSCode CoPilot Ehdotuksista/analyysissä/virheenkorjaamisessa/kommentoinnissa ja hienosäätämisessä.
## Lähteet, joita olet käyttänyt, vain ne joilla oli merkitystä työn kannalta.
https://materiaalit.github.io/intro-to-ai/
https://en.wikipedia.org/wiki/Markov_chain (ja sen materiaali yms.)
https://www.youtube.com/watch?v=i3AkTO9HLXo
https://algolabra-hy.github.io/ (ja sen materiaali)
