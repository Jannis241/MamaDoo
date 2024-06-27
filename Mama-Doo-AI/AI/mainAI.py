import Essen, Zutaten
import gmail
zutatenManager = Zutaten.Manager()
class MamaDooAi():
    def __init__(self):
        self.alleGerichte = Essen.alleGerichte
        

        self.nichtVorhandeneZutate = []
        self.loswerdeZutaten = []

    def evaluate(self, sortedByDifficulty = False, MamaBenötigtFilter = False):
        loswerdeBonus = 50
        sattMultiplier = .5
        ratingMultiplier = 1
        AufwandMultiplier = -2.5

        if sortedByDifficulty: 
            AufwandMultiplier = -1000
        
        possibleGerichte = {}  # gericht : score
        for gericht in self.alleGerichte:
            mamaTestÜberstanden = True
            if self.canEssenBeMade(gericht):

                isMamaNeeded = gericht.mamaBenötigt.lower().strip().replace(" ", "")

                # wenn 
                if (MamaBenötigtFilter):
                    print("is mama needed var: ", isMamaNeeded)
                    if (isMamaNeeded == "ja"):
                        
                        print(f"{gericht.name} hat den Mama nötig test nicht bestanden --> essen braucht mama: {gericht.mamaBenötigt}")
                        mamaTestÜberstanden = False
                if (mamaTestÜberstanden):
                    score = 0
                    for zutat in gericht.zutaten:
                        for loswerdeZutat in self.loswerdeZutaten:
                            if zutat.name == loswerdeZutat.name:
                                score += loswerdeBonus  # Punkte hinzufügen, wenn eine loswerdeZutat vorhanden ist

                    BewertungsScore = gericht.rating * ratingMultiplier
                    Sättigungsscore = gericht.satt * sattMultiplier
                    Aufwandscore = gericht.difficulty * AufwandMultiplier

                    score += BewertungsScore + Sättigungsscore + Aufwandscore
                            
                    possibleGerichte[gericht] = score
                
            
        
        # Sortiere possibleGerichte nach dem Score des Gerichts in absteigender Reihenfolge
        sorted_gerichte = sorted(possibleGerichte.keys(), key=lambda x: possibleGerichte[x], reverse=True)
        
        return sorted_gerichte
    
    def checkIfZutatExists(self, zutat):
        try:
            getattr(zutatenManager, zutat.strip().lower().replace(" ", "")) # veruschen die zutat im Manager zu finden, falls es sie nicht gibt, gibt es ein error
            return True
        except:
            return False

    def setUserInfo(self, loswerdeList, nichtVorhandenList):

        for zutatString in loswerdeList:
            self.loswerdeZutaten.append(getattr(zutatenManager, zutatString.strip().lower().replace(" ", "")))
        for zutatString in nichtVorhandenList:
            self.nichtVorhandeneZutate.append(getattr(zutatenManager, zutatString.strip().lower().replace(" ", "")))
    
        for zutat in self.nichtVorhandeneZutate:
            zutat.istVorhanden = -1
        for zutat in self.loswerdeZutaten:
            zutat.istVorhanden = 1
    
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
        print("")
        print(f"Checking: {essen.name}")
        for zutat in essen.zutaten:
            if self.getVorratOfZutat(zutat) == -1:
                vorhandenCheck = False
                print(f"{essen.name} failed vorhanden check, weil {zutat.name} nicht vorhanden ist!")
        print(f"{essen.name} hat den Vorhanden check geschafft")


        return vorhandenCheck

    
if __name__ == '__main__': # falls das programm manuell gestartet wird

    MDA = MamaDooAi()
    MDA.getUserInfo()
    results = MDA.evaluate() # Liste mit den Instanzen der möglichen Gerichte
    print()
    print()
    print(len(results), " Mögliche Gerichte gefunden!")
    print()
    info = "Das hier könnten die Gerichte für heute sein: "
    info += "\n"
    for gericht in results:
            Essen.printGerichtStats(gericht)
            info += "\n"
            info += f"Name: {gericht.name}"
            info += "\n"
            info += f"Bewertung: {gericht.rating}/10"
            info += "\n"
            info += f"Name: {gericht.satt}/10"
            info += "\n"
            info += f"Name: {gericht.difficulty}/10"
            info += "\n"
            info += f"Thermomix: {gericht.thermomix}"
            info += "\n"
            info += f"Mama benötigt: {gericht.mamaBenötigt}"
            info += "\n"
            info += f"Wann: {gericht.wann}"
            info += "\n"
            info += "Zutaten: "
            for zutat in gericht.zutaten:
                info += zutat.name +", "
            info += "\n"
            info += f"Extra Info: {gericht.extraInfo}"
            info += "\n"
            info += "\n"
    if len(results) != 0:
        #gmail.sendMail(info, f"Mama Doo AI - Essen für Heute - {date.today().strftime("%d-%m-%Y")}")
        pass
else: # falls es ein import ist
    print()
    print()
    print()
    print()
    print("Main AI got imported..")
    print()
    MDA = MamaDooAi()








    