# Was ist der Erwartungswert für die Augensumme beim Würfeln mit 6 Würfeln?

"""
Der "Erwartungswert" (Expected Value) in der Wahrscheinlichkeitsrechnung ist ein Maß dafür, 
was man "im Durchschnitt" erwarten kann, wenn ein Zufallsexperiment unter identischen 
Bedingungen sehr oft wiederholt wird. 

Es ist ein gewichtetes Mittel aller möglichen Ergebnisse, 
wobei die Gewichtung auf der Wahrscheinlichkeit jedes Ergebnisses basiert. 

Mathematisch wird der Erwartungswert als die Summe der Produkte aus 
jedem möglichen Ergebnis und seiner Wahrscheinlichkeit berechnet. 

Wem das zu kompliziert ist, der kann sich dem Erwartungswert auch experimentell
mit einem Python Programm annähern.

"""
import random

anzahl_experimente = 1
total = 0

for experiment in range(anzahl_experimente):
    sum = 0
    for dice in range(6):
        sum += random.randint(1, 6)
    total += sum

print("Erwartungswert: ", total/anzahl_experimente)
