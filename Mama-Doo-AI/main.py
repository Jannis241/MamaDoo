import Essen, Zutaten



class MamaDooAi():
    def __init__(self):
        self.alleGerichte = Essen.alleGerichte
        

        self.nichtVorhandeneZutate = []
        self.loswerdeZutaten = []

    def evaluate(self):
        possibleGerichte = []
        for gericht in self.alleGerichte:
            if (self.canEssenBeMade(gericht)):
                
                possibleGerichte.append(gericht)

        return possibleGerichte
    
    def getUserInfo(self):
        
        while True:
            loswerden = input("Welche Lebensmittel möchtest du loswerden (q wenn du fertig bist): ").strip().lower().replace(" ", "")
            if (loswerden == "q"):
                break
            try:
                self.loswerdeZutaten.append(getattr(zutatenManager, loswerden))
            except:
                print(loswerden, "wurde nicht gefunden.")
        print()
        while True:
            nicht = input("Welche Lebensmittel hast du nicht(q wenn du fertig bist): ").strip().lower().replace(" ", "")
            if (nicht == "q"):
                break
            try:
                self.nichtVorhandeneZutate.append(getattr(zutatenManager, nicht))
            except:
                print(nicht, "wurde nicht gefunden.")

        for zutat in self.nichtVorhandeneZutate:
            zutat.istVorhanden = -1
        for zutat in self.loswerdeZutaten:
            zutat.istVorhanden = 1
        print()
        print("Super, ich berechne dir dafür jetzt die Gerichte!")

    def getVorratOfZutat(self, zutat):
        return getattr(zutatenManager, zutat.name).istVorhanden

    def canEssenBeMade(self, essen):
        vorhandenCheck = True
        loswerdeCheck = False
        print("")
        print(f"Checking: {essen.name}")
        for zutat in essen.zutaten:
            if self.getVorratOfZutat(zutat) == -1:
                vorhandenCheck = False
                print(f"{essen.name} failed vorhanden check, weil {zutat.name} nicht vorhanden ist!")
        print(f"{essen.name} hat den Vorhanden check geschafft")
        for loswerdeZutat in self.loswerdeZutaten:
            for zutat in essen.zutaten:
                if zutat.name == loswerdeZutat.name:
                    loswerdeCheck = True
                    print(f"{essen.name} failed loswerde check, weil {zutat.name} nicht benutzt wird!")

        print(f"{essen.name} hat den loswerde check geschafft")
        return vorhandenCheck == True and loswerdeCheck == False

zutatenManager = Zutaten.Manager()



MDA = MamaDooAi()
MDA.getUserInfo()
results = MDA.evaluate() # Liste mit den Instanzen der möglichen Gerichte

print()
print()
print(len(results), " Mögliche Gerichte gefunden!")
print()
for gericht in results:
    Essen.printGerichtStats(gericht)

input()





    