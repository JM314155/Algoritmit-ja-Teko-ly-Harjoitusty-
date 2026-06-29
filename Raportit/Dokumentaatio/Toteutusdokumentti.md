# Toteutusdokumentti
## Ohjelman yleisrakenne
Ohjelma on jaettu käyttöliittymästä huolehtivaan tiedostoon (main.py) sekä tekoälyn logiikasta huolehtiviin luokkiin (src/model hakemisto). Tekoäly on jaettu itsenäisiin moduuleihin: MarkovChain, FrequencyAnalysis ja PatternMatcher. Pääluokka Sum toimii ensemblienä, joka kerää näiltä moduuleilta ennusteet sekö suorittaa äänestyksen ja päättää lopullisen siirron.
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

## Laajennus: Markovin ketjujen kertaluvut ja Multi-Markov

Projekti laajennettiin kahdella uudella luokalla: MarkovOrder ja MultiMarkov.

**MarkovOrder** on yleistetty versio alkuperäisestä MarkovChain-luokasta. Ainoa rakenteellinen ero on, että tila ei ole enää yksittäinen merkkijono vaan tuple edellisistä siirroista:

*   Alkuperäinen: `self.matrix['Kivi']['Sakset'] = 4`
*   Laajennettu: `self.transitions[('Kivi', 'Sakset')]['Paperi'] = 2`

Tämä mahdollistaa minkä tahansa kertaluvun ilman erillisiä luokkia. Alkuperäinen MarkovChain jätettiin koskemattomaksi yhteensopivuuden vuoksi.

**MultiMarkov** pitää sisällään viisi MarkovOrder-instanssia (kertaluvut 1–5) sekä fokuspituus-valitsimen. Se toimii rinnakkaisena järjestelmänä alkuperäisen Sum-luokan kanssa eikä korvaa sitä. Fokuspituus F määrää kuinka monen viimeisen kierroksen pisteiden perusteella paras malli valitaan ennustamaan seuraava siirto.

### Aika- ja tilavaativuudet (uudet luokat)

*   **MarkovOrder:**
    - Aikavaativuus: O(N) päivittämisessä, missä N on kertaluku (listan siivutus tuple(history[-N:])). Koska N on pieni vakio (max 5), käytännössä O(1).
    - Tilavaativuus: O(3^N) — mahdollisia tuple-avaimia on 3^N kappaletta. Kertaluvulla 5 tiloja on 243, joten muistinkäyttö pysyy pienenä.
*   **MultiMarkov:**
    - Aikavaativuus: O(F) per kierros, missä F on fokuspituus (pisteiden summaukseen). Käytännössä O(1) koska F on pieni vakio.
    - Tilavaativuus: O(T) missä T on pelattujen kierrosten määrä (pistelista kasvaa).

### Tilaharvarautuminen (state sparsity)

Kertaluvun kasvattaminen lisää mahdollisten tilojen määrää eksponentiaalisesti. 300 kierroksen pelissä kertaluvulla 5 yksittäinen tila nähdään keskimäärin vain  noin 1,2 kertaa, joten malli on useimmiten satunnainen. MultiMarkov hyödyntää fokuspituus-valitsinta juuri tästä syystä: korkea kertaluku saa ennustaa vain kun sillä on riittävästi dataa.

## Työn mahdolliset puutteet ja parannusehdotukset
Tällä hetkellä Sum luokka käyttää aika yksinkertaista enemmistöäänestystä, Vaikka ohjelma pitää kirjaa moduulien osumatarkkuudesta (self.wins), tätä dataa ei vielä aktiivisesti käytetä painottamaan parhaiten pärjäävän moduulin ääntä. Jatkossa algoritmi voisi antaa suuremman painoarvon sille tekoälylle, jolla on suurin osumaprosentti. Olisi myös voinut lisätä esim. pisteytys algoritmin joka olisi pisteteyttänyt algortimit ja sen avulla pystyisi ennustamaan paremmin tulevia huomioimalla aikeisemmat erehdykset. Tämä on toteutettu MultiMarkov-laajennuksessa, joka valitsee kokonaan parhaan mallin äänestämisen sijaan.
## Laajojen kielimallien (ChatGPT yms.) käyttö. Mainitse mitä mallia on käytetty ja miten. Mainitse myös mikäli et ole käyttänyt. Tämä on tärkeää!
Yliopiston Currechattia/GPT on käytetty koodin virheanalyysissa sekä koodin korjaamisessa sekä tiivistämisessä/siistimisessä/optimoinnissa sekä kääntämisessä
VSCode CoPilot/Claude Ehdotuksista/analyysissä/virheenkorjaamisessa/kommentoinnissa ja hienosäätämisessä.
## Lähteet, joita olet käyttänyt, vain ne joilla oli merkitystä työn kannalta.
https://materiaalit.github.io/intro-to-ai/
https://en.wikipedia.org/wiki/Markov_chain (ja sen materiaali yms.)
https://www.youtube.com/watch?v=i3AkTO9HLXo
https://algolabra-hy.github.io/ (ja sen materiaali)
Wang, L., Huang, W., Li, Y., Evans, J. & He, S. (2020). Multi-AI competing and winning against humans in iterated Rock-Paper-Scissors game. Scientific Reports, 10, 13873. https://arxiv.org/pdf/2003.06769
