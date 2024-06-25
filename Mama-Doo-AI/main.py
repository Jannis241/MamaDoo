import Essen, Zutaten



class MamaDooAi():
    def __init__(self):
        self.alleGerichte = Essen.alleGerichte
        

        self.nichtVorhandeneZutate = [zutatenManager.kartoffeln]
        self.loswerdeZutaten = []
        for zutat in self.nichtVorhandeneZutate:
            zutat.istVorhanden = -1

        self.possibleGerichte = []
        for gericht in self.possibleGerichte:
            if self.canEssenBeMade(gericht):
                self.possibleGerichte.append(gericht)
        for pg in self.possibleGerichte:
            print(pg.name)

    def evaluate(self):
        return []
    
    def getUserInfo(self):
        pass

    def canEssenBeMade(self, essen):
        for zutat in essen.zutaten:
            if zutat.istVorhanden == -1:
                return False
            
        return True

zutatenManager = Zutaten.Manager()



MDA = MamaDooAi()
MDA.getUserInfo()



results = MDA.evaluate() # Liste mit den Instanzen der möglichen Gerichte





    