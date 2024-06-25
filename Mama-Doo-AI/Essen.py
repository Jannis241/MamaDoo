import Zutaten
import os
import csv
class Essen:
    def __init__(self, name, rating, satt, difficulty, zutaten, wann, tm, MamaBenötigt, addOns=None):
        self.name = name
        self.rating = rating
        self.satt = satt
        self.difficulty = difficulty
        self.zutaten = zutaten
        self.addOns = addOns
        self.wann = wann
        self.thermomix = tm 
        self.mamaBenötigt = MamaBenötigt


alleGerichte = []

def read_configurations(filename):
    gerichte = []
    zutatenManager = Zutaten.Manager()
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line and line[0] != "#":
                    parts = line.split(',')
                    
                    name = parts[0].strip().lower()
                    rating = float(parts[1].strip())
                    satt = float(parts[2].strip())
                    difficulty = float(parts[3].strip())
                    wann = parts[4].strip().lower()
                    zutatenListe = []
                    tm = parts[5].strip().lower()
                    mb = parts[6].strip().lower()
                    for i in range(7, len(parts)):
                        word = parts[i].strip().lower()
                        zutatenListe.append(word)
                
                    acutalZutatenListe = []
                    for zutat_name in zutatenListe:
                        zutat = getattr(zutatenManager, zutat_name.strip())
                        acutalZutatenListe.append(zutat)
                    
                    essen = Essen(name, rating, satt, difficulty, acutalZutatenListe, wann, tm, mb)
                    alleGerichte.append(essen)

    except FileNotFoundError:
        print(f"Datei {filename} wurde nicht gefunden.")
    
    return gerichte

# Beispielaufruf
script_dir = os.path.dirname(__file__)
filename = os.path.join(script_dir, 'config.txt')
read_configurations(filename)

for gericht in alleGerichte:
    print(f"Name: {gericht.name}")
    print(f"Bewertung: {gericht.rating}")
    print(f"Sättigung: {gericht.satt}")
    print(f"Schwierigkeit: {gericht.difficulty}")
    print(f"Zutaten: {[zutat.name + ": " + str(zutat.istVorhanden) for zutat in gericht.zutaten]}")
    print(f"Wann: {gericht.wann}")
    print(f"Thermomix: " + gericht.thermomix)
    print(f"Mama benötigt: " + gericht.thermomix)
    print(f"")



