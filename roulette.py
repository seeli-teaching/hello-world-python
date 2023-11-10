# Was ist der Erwartungswert (Gewinnerwartung) für ein Roulettespiel,
# wenn ich immer einen Franken auf "Gerade" setze?

import random

anzahl_spiele = 1
gewinn = 0

for spiel in range(anzahl_spiele):
    resultat = random.randint(1, 36)
    # if resultat == 0:
    #    continue
    if resultat % 2 == 0:
        gewinn += 2


print("Gewinnerwartung: ", gewinn/anzahl_spiele,
      "Gewinn absolut: ", gewinn - anzahl_spiele)
