import Essen, Zutaten



class MamaDooAi():
    def __init__(self):
        self.alleGerichte = []
        self.alleZutaten = []
        self.vorhandeneZutaten = []
    
    def evaluate(self):
        return []
    
    def getUserInfo(self):
        pass

    def canEssenBeMade(self, essen):
        for zutat in essen.zutaten:
            if not zutat in self.vorhandeneZutaten:
                return False
            
        return True

zutatenManager = Zutaten.Manager()



MDA = MamaDooAi()
MDA.getUserInfo()



results = MDA.evaluate() # Liste mit den Instanzen der möglichen Gerichte





    