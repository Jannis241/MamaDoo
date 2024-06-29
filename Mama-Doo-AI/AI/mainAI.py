
import Essen
import Zutaten

import gmail



class MamaDooAi():
    def __init__(self):
        print("initializing MamaDooAi..")
        self.alleGerichte = Essen.alleGerichte
        self.zutatenManager = Zutaten.Manager()
        self.nichtVorhandeneZutate = []
        self.loswerdeZutaten = []

    def evaluate(self, sortedByDifficulty=False, MamaBenötigtFilter=False, sortedByRating=False, sortedByGesund=False, sortedBySatt=False):
        validGerichteCount = 0
        
        loswerdeBonus = 100000
        sattMultiplier = 1
        gesundMultiplier = 1.5
        ratingMultiplier = 2
        AufwandMultiplier = -1.5

        mamaTest = True

        if sortedByDifficulty:
            AufwandMultiplier = -100
        if sortedByRating:
            ratingMultiplier = 100
        if sortedByGesund:
            gesundMultiplier = 100
        if sortedBySatt:
            sattMultiplier = 100

        possibleGerichte = {}  # gericht : score
        for gericht in self.alleGerichte:
            score = 0
            if self.canEssenBeMade(gericht):  # alle zutaten sind da

                # mama check funktioniert noch nicht
                if MamaBenötigtFilter:
                    mamaTest = gericht.mamaBenötigt.lower().strip().replace(" ", "") == "nein"

                if mamaTest:
                    # desto mehr der Aufwand ist desto mehr geht der aufwand score ins negative
                    aufwandScore = gericht.difficulty * AufwandMultiplier
                    ratingScore = gericht.rating * ratingMultiplier
                    sattScore = gericht.satt * sattMultiplier
                    gesundScore = gericht.gesund * gesundMultiplier

                    score += aufwandScore + ratingScore + sattScore + gesundScore

                    for zutat in gericht.zutaten:
                        for loswerdeZutat in self.loswerdeZutaten:
                            if zutat.name == loswerdeZutat.name:
                                score += loswerdeBonus

                    possibleGerichte[gericht] = score
                    validGerichteCount += 1

        if len(possibleGerichte) != validGerichteCount:
            raise KeyError("Something went wrong the evaluation dict")

        sorted_gerichte = sorted(possibleGerichte.keys(), key=lambda x: possibleGerichte[x], reverse=True)
        for gericht in sorted_gerichte:
            print(f"Name: {gericht.name} -> {possibleGerichte[gericht]}")
        print()

        print("AI found", len(sorted_gerichte), "possibilities..")
        print(len(self.alleGerichte) - len(sorted_gerichte), "got sorted out..")
        print()

        return sorted_gerichte

    def reinit(self):
        # alle zutaten werden resetet falls der user nochmal neue angaben machen möchte
        for zutat in self.loswerdeZutaten:
            zutat.reset()

        for zutat in self.nichtVorhandeneZutate:
            zutat.reset()

        # init alle variablen neu falls der user noch einmal von vorne anfängt
        self.loswerdeZutaten = []
        self.nichtVorhandeneZutate = []
        self.alleGerichte = Essen.alleGerichte
        print("Reseted AI parameters...")

    def checkIfZutatExists(self, zutat):
        try:
            # veruschen die zutat im Manager zu finden, falls es sie nicht gibt, gibt es ein error
            getattr(self.zutatenManager, zutat.strip().lower().replace(" ", ""))
            return True
        except:
            return False

    def setUserInfo(self, loswerdeList, nichtVorhandenList):
        for zutatString in loswerdeList:
            self.loswerdeZutaten.append(
                getattr(self.zutatenManager, zutatString.strip().lower().replace(" ", "")))
        for zutatString in nichtVorhandenList:
            self.nichtVorhandeneZutate.append(
                getattr(self.zutatenManager, zutatString.strip().lower().replace(" ", "")))

        for zutat in self.loswerdeZutaten:
            zutat.istVorhanden = 1
        for zutat in self.nichtVorhandeneZutate:
            zutat.istVorhanden = -1

    def getVorratOfZutat(self, zutat):
        return getattr(self.zutatenManager, zutat.name).istVorhanden

    def canEssenBeMade(self, essen):
        for zutat in essen.zutaten:
            if self.getVorratOfZutat(zutat) == -1:
                print(f"{essen.name} failed because of: vorhanden Check ({zutat.name})")
                return False
        return True


MDA = MamaDooAi()



