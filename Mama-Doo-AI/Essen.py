import Zutaten
import os

class Essen:
    def __init__(self, name, rating, satt, difficulty, zutaten, addOns=None):
        self.name = name
        self.rating = rating
        self.satt = satt
        self.difficulty = difficulty
        self.zutaten = zutaten
        self.addOns = addOns


def read_configurations(filename):
    gerichte = []
    zutatenManager = Zutaten.Manager()
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    name = parts[0].strip()
                    rating = float(parts[1].strip())
                    satt = float(parts[2].strip())
                    difficulty = float(parts[3].strip())
                    zutaten_liste = parts[4].strip()[1:-1].split(',')
                    zutaten = []

                    for zutat_name in zutaten_liste:
                        try:
                            zutat = getattr(zutatenManager, zutat_name.strip())
                            zutaten.append(zutat)
                        except AttributeError:
                            pass
                    
                    gericht = Essen(name, rating, satt, difficulty, zutaten)
                    gerichte.append(gericht)

    except FileNotFoundError:
        print(f"Datei {filename} wurde nicht gefunden.")
    
    return gerichte

script_dir = os.path.dirname(__file__)
filename = os.path.join(script_dir, 'config.txt')
gerichte = read_configurations(filename)

for gericht in gerichte:
    print(f"Name: {gericht.name}")
    print(f"Bewertung: {gericht.rating}")
    print(f"Sättigung: {gericht.satt}")
    print(f"Schwierigkeit: {gericht.difficulty}")
    print(f"Zutaten: {[zutat.name for zutat in gericht.zutaten]}")
    print()