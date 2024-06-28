import Zutaten
import os
class Essen:
    def __init__(self, name, rating, satt, difficulty, gesund, zutaten, wann, tm, MamaBenötigt, extraInfo, addOns=None, ):
        self.name = name
        self.rating = rating
        self.satt = satt
        self.difficulty = difficulty
        self.zutaten = zutaten
        self.addOns = addOns
        self.wann = wann
        self.thermomix = tm 
        self.mamaBenötigt = MamaBenötigt
        self.extraInfo = extraInfo
        self.gesund = gesund


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
                    
                    name = parts[0].strip()
                    rating = float(parts[1].strip())
                    satt = float(parts[2].strip())
                    difficulty = float(parts[3].strip())
                    gesund = float(parts[4].strip())
                    wann = parts[5].strip()
                    zutatenListe = []
                    tm = parts[6].strip()
                    mb = parts[7].strip()
                    extraInfo = parts[8].strip()
                    
                    for i in range(9, len(parts)):
                        word = parts[i].strip().lower()
                        zutatenListe.append(word)
                
                    acutalZutatenListe = []
                    for zutat_name in zutatenListe:
                        try:
                            zutat = getattr(zutatenManager, zutat_name.strip())
                            
                            acutalZutatenListe.append(zutat)
                            
                        except:
                            print()
                            print("Zutat", zutat_name, "does not exist.")
                            exit()
                    
                    essen = Essen(name, rating, satt, difficulty, gesund, acutalZutatenListe, wann, tm, mb, extraInfo)
                    alleGerichte.append(essen)
    
    except FileNotFoundError:
        print(f"Datei {filename} wurde nicht gefunden.")
    
    return gerichte


script_dir = os.path.dirname(__file__)
filename = os.path.join(script_dir, 'config.txt')
read_configurations(filename)

def printGerichtStats(gericht):
    print(f"Name: {gericht.name}")
    print(f"Bewertung: {gericht.rating}")
    print(f"Sättigung: {gericht.satt}")
    print(f"Schwierigkeit: {gericht.difficulty}")
    print(f"Zutaten: {[zutat.name + ": " + str(zutat.istVorhanden) for zutat in gericht.zutaten]}")
    print(f"Wann: {gericht.wann}")
    print(f"Thermomix: " + gericht.thermomix)
    print(f"Mama benötigt: " + gericht.mamaBenötigt)
    print(f"Extra info: " + gericht.extraInfo)
    print(f"")



