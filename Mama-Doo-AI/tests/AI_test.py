import sys
sys.path.append('./AI')
import Essen
import Zutaten
import mainAI
import unittest

class TestMamaDooAi(unittest.TestCase):

    def test_reset_loswerde_ingredients(self):
        # Arrange
        mama_doo_ai = mainAI.MamaDooAi()
        loswerde_ingredient = Zutaten.Zutat("milch")
        mama_doo_ai.loswerdeZutaten.append(loswerde_ingredient)

        # Act
        mama_doo_ai.reinit()

        # Assert
        assert loswerde_ingredient.istVorhanden == 0


    def test_reset_nicht_vorhandene_ingredients(self):
        # Arrange
        mama_doo_ai = mainAI.MamaDooAi()
        nicht_vorhandene_ingredient = Zutaten.Zutat("milch")
        mama_doo_ai.nichtVorhandeneZutate.append(nicht_vorhandene_ingredient)

        # Act
        mama_doo_ai.reinit()

        # Assert
        assert nicht_vorhandene_ingredient.istVorhanden == 0


    def test_clear_loswerde_ingredients(self):
        # Arrange
        mama_doo_ai = mainAI.MamaDooAi()
        loswerde_ingredient = Zutaten.Zutat("milch")
        mama_doo_ai.loswerdeZutaten.append(loswerde_ingredient)

        # Act
        mama_doo_ai.reinit()

        # Assert
        assert len(mama_doo_ai.loswerdeZutaten) == 0


    def test_clear_nicht_vorhandene_ingredients(self):
        # Arrange
        mama_doo_ai = mainAI.MamaDooAi()
        nicht_vorhandene_ingredient = Zutaten.Zutat("milch")
        mama_doo_ai.nichtVorhandeneZutate.append(nicht_vorhandene_ingredient)

        # Act
        mama_doo_ai.reinit()

        # Assert
        assert len(mama_doo_ai.nichtVorhandeneZutate) == 0


    def test_reset_all_recipes(self):

        # Arrange
        mama_doo_ai = mainAI.MamaDooAi()
        mama_doo_ai.alleGerichte = ["fortnite", "fortnite", "fortnite", "fortnite", "fortnite"]

        # Act
        mama_doo_ai.reinit()

        # Assert
        assert mama_doo_ai.alleGerichte == Essen.alleGerichte







    def test_check_if_ingredient_exists(self):
        # Arrange
        mama_doo_ai = mainAI.MamaDooAi()
        test1 = mama_doo_ai.checkIfZutatExists("fortnite")
        test2 = mama_doo_ai.checkIfZutatExists("sgjksdfsfd")
        test3 = mama_doo_ai.checkIfZutatExists("milch")
        test4 = mama_doo_ai.checkIfZutatExists("kartoffeln")

        assert test1 == False
        assert test2 == False
        assert test3 == True
        assert test4 == True



    def test_userInfo(self):
        mda = mainAI.MamaDooAi()
        mda.setUserInfo(["milch", "kartoffeln", "wasser"], ["reis", "nutella"])
        assert len(mda.loswerdeZutaten) == 3
        assert len(mda.nichtVorhandeneZutate) == 2
        assert mda.loswerdeZutaten[0].name == "milch"
        assert mda.loswerdeZutaten[1].name == "kartoffeln"
        assert mda.loswerdeZutaten[2].name == "wasser"
        assert mda.nichtVorhandeneZutate[0].name == "reis"
        assert mda.nichtVorhandeneZutate[1].name == "nutella"
        assert mda.loswerdeZutaten[0].istVorhanden != 0
        assert mda.loswerdeZutaten[0].istVorhanden == 1
        assert mda.loswerdeZutaten[1].istVorhanden == 1
        assert mda.loswerdeZutaten[2].istVorhanden == 1
        assert mda.nichtVorhandeneZutate[0].istVorhanden == -1
        assert mda.nichtVorhandeneZutate[1].istVorhanden == -1
        assert mda.nichtVorhandeneZutate[0].istVorhanden != 0


    def test_setUserInfo_valid_lists(self):
        loswerdeList = ["kartoffeln", "mehl"]
        nichtVorhandenList = ["milch", "zucker"]
        mama_doo_ai = mainAI.MamaDooAi()
        mama_doo_ai.setUserInfo(loswerdeList, nichtVorhandenList)
        assert len(mama_doo_ai.loswerdeZutaten) == 2
        assert len(mama_doo_ai.nichtVorhandeneZutate) == 2
        assert all(zutat.istVorhanden == 1 for zutat in mama_doo_ai.loswerdeZutaten)
        assert all(zutat.istVorhanden == -1 for zutat in mama_doo_ai.nichtVorhandeneZutate)


    def test_setUserInfo_empty_lists(self):
        loswerdeList = []
        nichtVorhandenList = []
        mama_doo_ai = mainAI.MamaDooAi()
        mama_doo_ai.setUserInfo(loswerdeList, nichtVorhandenList)
        assert len(mama_doo_ai.loswerdeZutaten) == 0
        assert len(mama_doo_ai.nichtVorhandeneZutate) == 0


    def test_setUserInfo_invalid_zutat_names(self):
        loswerdeList = ["invalid_zutat", "mehl"]
        nichtVorhandenList = ["milc h", "invalid_zutat"]
        mama_doo_ai = mainAI.MamaDooAi()
        try:
            mama_doo_ai.setUserInfo(loswerdeList, nichtVorhandenList)
            assert False
        except AttributeError as e:
            assert True





    def test_setUserInfo_mixed_case_and_spaces(self):
        loswerdeList = ["KARTOFFELn", "mehl ", " KARTO FFELn"]
        nichtVorhandenList = ["MILCH", " Zucker ", " MIL CH"]
        mama_doo_ai = mainAI.MamaDooAi()
        mama_doo_ai.setUserInfo(loswerdeList, nichtVorhandenList)
        assert len(mama_doo_ai.loswerdeZutaten) == 3
        assert len(mama_doo_ai.nichtVorhandeneZutate) == 3
        assert all(zutat.istVorhanden == 1 for zutat in mama_doo_ai.loswerdeZutaten)
        assert all(zutat.istVorhanden == -1 for zutat in mama_doo_ai.nichtVorhandeneZutate)




    def test_get_vorrat_of_nicht_vorhandene_zutat(self):

        MDA = mainAI.MamaDooAi()
        zutatenManager = Zutaten.Manager()
        fortnite = zutatenManager.mehl
        fortnite.istVorhanden = -1
        assert MDA.getVorratOfZutat(fortnite) == -1
    
    
    
    def test_get_vorrat_of_valid_zutat(self):
        MDA = mainAI.MamaDooAi()
        zutatenManager = Zutaten.Manager()
        fortnite = zutatenManager.mehl
        fortnite.istVorhanden = 1



    
        zutat3 = zutatenManager.garnelen
        assert MDA.getVorratOfZutat(zutat3) == 0
        assert MDA.getVorratOfZutat(fortnite) == 1
        
    def test_get_vorrat_of_invalid_zutat(self):
        MDA = mainAI.MamaDooAi()
        try:
            MDA.getVorratOfZutat("invalid")
            assert False
        except AttributeError as e:
            assert True

    def test_get_default_vorrat_of_zutat(self):
        MDA = mainAI.MamaDooAi()
        zm = Zutaten.Manager()
        zutat = zm.möhren

        assert MDA.getVorratOfZutat(zutat) == 0



    def test_get_vorrat_of_uninitialized_zutat(self):
        MDA = mainAI.MamaDooAi()
        zm = Zutaten.Manager()
        zutat = zm
        try:
            MDA.getVorratOfZutat(zutat)
            assert False
        except:
            assert True
        


    def test_if_essen_can_be_made_valid_gericht(self):
        MDA = mainAI.MamaDooAi()
        gericht0 = Essen.alleGerichte[0]
        zm = Zutaten.Manager()
        gericht1 = Essen.Essen("testEssen1", 5,3,2,1, [zm.kartoffeln, zm.eier], "sdf", "ja", "ja", "-")
        gericht2 = Essen.Essen("testEssen2", 5,3,2,1, [zm.reis, zm.chickennuggets], "sdf", "ja", "ja", "-")
        gericht3 = Essen.alleGerichte[8]
        gericht4 = Essen.alleGerichte[10]

        zm.kartoffeln.istVorhanden = 1
        assert MDA.canEssenBeMade(gericht0) == True
        assert MDA.canEssenBeMade(gericht1) == True
        assert MDA.canEssenBeMade(gericht2) == True
        assert MDA.canEssenBeMade(gericht3) == True
        assert MDA.canEssenBeMade(gericht4) == True



    def test_if_essen_can_be_made_invalid_gericht(self):
        MDA = mainAI.MamaDooAi()
        zm = Zutaten.Manager()
        mehl = zm.mehl
        mehl.istVorhanden = -1
        
        eier = zm.eier
        eier.istVorhanden = -1
        
        chickennuggets = zm.chickennuggets
        chickennuggets.istVorhanden = -1

        reis = zm.reis
        reis.istVorhanden = -1

        gericht0 = Essen.Essen("testEssen", 5,3,2,1, [zm.mehl, zm.milch], "sdf", "ja", "ja", "-")
        gericht1 = Essen.Essen("testEssen1", 5,3,2,1, [zm.kartoffeln, zm.eier], "sdf", "ja", "ja", "-")
        gericht2 = Essen.Essen("testEssen2", 5,3,2,1, [zm.reis, zm.chickennuggets], "sdf", "ja", "ja", "-")


        assert MDA.canEssenBeMade(gericht0) == False
        assert MDA.canEssenBeMade(gericht1) == False
        assert MDA.canEssenBeMade(gericht2) == False




