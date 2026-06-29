# Määrittelydokumentti
## Mitä ohjelmointikieltä käytät?
Käytän pääosin pythonia 
## Kerro myös mitä muita kieliä hallitset siinä määrin, että pystyt tarvittaessa vertaisarvioimaan niillä tehtyjä projekteja.
Tiedän jonkin verran c++ tai c# 
## Mitä algoritmeja ja tietorakenteita toteutat työssäsi?
Työssä käytetään siirtojen ennakointiin Taajuusanalyysia, Markov-mallia ja yleistä kuvio tunnistus algoritmia. Näitä painotetaan algoritmiin Wang et al menetelmän avulla, joka ottaa huomioon datan määrä siitä painotuksen. Laajennuksena toteutettiin MarkovOrder (kertaluvut 5 asti) sekä MultiMarkov-valitsin, joka toteuttaa Wang et al. dynaamisen mallinvalinnan fokuspituus-ikkunalla.
Tietorakenteista lista, sanakirja ja ehkä numpy avulla matriisit
## Minkä ongelman ratkaiset?
Tavoitteena on tehdä algoritmi, joka pystyy oppimaan/päättelemään pelaajan todennäköiset seuraavat siirrot
## Mitä syötteitä ohjelma saa ja miten niitä käytetään?
Pelaajan siirto/aiemmat siirrot ja ehkä voi säätää vaikeustasoa
## Tavoitteena olevat aika- ja tilavaativuudet (esim. O-analyysit)
Tila/aikavaatimus tarkoitus olisi olla O(1), koska pelissä ei ole huomattavasti siirtovaihtoehtoja, ehkä pitemmässä pelissä voi olla hitaampaa, mutta pyrkimys O(1)
## Lähteet, joita aiot käyttää
Lähteet löytyy toteutus dokumentissa
## Harjoitustyön Ydin. Kuvaile määrittelydokumenttiin muutamalla lauseella, mikä on aiheesi ydin. Käytä tähän aikaa koska se auttaa harjoitustyön toteuttamisessa. Vaikka koko työhön tarvitaan muutakin kuin sen ytimeen liittyvää koodia, suurin osa kehitykseen käytettävästä ajasta pitäisi kuluttaa juurikin ytimen kehitykseen. Suunnittele ajankäyttösi niin.
Harjoitustyön ydin on toteuttaa Kivi–sakset–paperi peliin älykäs tietokonevastustaja, joka oppii pelaajan käyttäytymisestä ja pyrkii voittamaan ennakoimalla tulevia siirtoja. Tekoäly perustuu yksinkertaisiin tilastollisiin menetelmiin, kuten taajuusanalyysiin ja Markovin ketjuihin. Työn pääpaino on algoritmin kehittämisessä, joka analysoi pelaajan historiaa ja valitsee sen perusteella optimaalisen vastasiirron
