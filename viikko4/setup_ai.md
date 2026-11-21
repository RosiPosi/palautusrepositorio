Poistiko agentti toisteisuuden mielestäsi järkevästi? Onko testikoodi nyt helpommin luettavaa?
- Agentti editoi koodin järkevästi ja se on helpompi ja lyhyempää luettavaa.
Muuttiko agentti testien toiminnallisuutta, esim. poistiko tai heikensikö se tarkistuksia (assert_called_with vs. assert_called)?
- Agentti piti testin toiminnallisuuden samana ja piri myös assert_called_with samana. Se ei heikentänyt tarkistusta ja poisti osat, jotka lisäsivät toisteisuutta. Se kuitenkin piti saman konseptin.
Jouduitko korjaamaan agentin tekemiä muutoksia itse tai pyytämään siltä muutoksia? Mitä ja miksi?
- Minun ei täytynyt korjata mitään, sillä koodi toimi kuin piti ja se läpäisi kaikki pytest testit. Koodi myös näytti siistiltä eikä ollut mitään epäselvää. Kuitenkin, jos aikoo käyttää tekoälyä koodaamisessa, tulisi olla hyvin tuttu sen muutoksiin, jotta niihin voi palata myöhemminkin.