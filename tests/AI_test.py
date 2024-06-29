import sys
import unittest
from unittest.mock import patch

from AI import Essen, Zutaten, mainAI


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
        zutatenManager = MDA.zutatenManager
        mehl = zutatenManager.mehl
        mehl.istVorhanden = -1

        assert mehl.istVorhanden == -1
        assert MDA.getVorratOfZutat(mehl) == -1

    def test_get_vorrat_of_valid_zutat(self):
        MDA = mainAI.MamaDooAi()
        zutatenManager = MDA.zutatenManager

        mehl = zutatenManager.mehl
        mehl.istVorhanden = 1

        zucker = zutatenManager.zucker

        assert MDA.getVorratOfZutat(mehl) == 1
        assert MDA.getVorratOfZutat(zucker) == 0

    def test_get_vorrat_of_invalid_zutat(self):
        MDA = mainAI.MamaDooAi()
        try:
            MDA.getVorratOfZutat("invalid")
            assert False
        except AttributeError as e:
            assert True

    def test_get_default_vorrat_of_zutat(self):
        MDA = mainAI.MamaDooAi()
        zutatenManager = MDA.zutatenManager
        zutat = zutatenManager.möhren

        assert MDA.getVorratOfZutat(zutat) == 0

    def test_get_vorrat_of_uninitialized_zutat(self):
        MDA = mainAI.MamaDooAi()
        zutatenManager = MDA.zutatenManager
        zutat = zutatenManager
        try:
            MDA.getVorratOfZutat(zutat)
            assert False
        except:
            assert True

    def test_if_essen_can_be_made_valid_gericht(self):
        MDA = mainAI.MamaDooAi()
        zutatenManager = MDA.zutatenManager
        gericht0 = Essen.alleGerichte[0]
        gericht1 = Essen.Essen("testEssen1", 5, 3, 2, 1, [zutatenManager.kartoffeln, zutatenManager.eier], "sdf", "ja", "ja", "-")
        gericht2 = Essen.Essen("testEssen2", 5, 3, 2, 1, [zutatenManager.reis, zutatenManager.chickennuggets], "sdf", "ja", "ja", "-")
        gericht3 = Essen.alleGerichte[8]
        gericht4 = Essen.alleGerichte[10]

        zutatenManager.kartoffeln.istVorhanden = 1
        assert MDA.canEssenBeMade(gericht0) == True
        assert MDA.canEssenBeMade(gericht1) == True
        assert MDA.canEssenBeMade(gericht2) == True
        assert MDA.canEssenBeMade(gericht3) == True
        assert MDA.canEssenBeMade(gericht4) == True

    def test_if_essen_can_be_made_invalid_gericht(self):
        MDA = mainAI.MamaDooAi()
        zutatenManager = MDA.zutatenManager

        mehl = zutatenManager.mehl
        mehl.istVorhanden = -1

        eier = zutatenManager.eier
        eier.istVorhanden = -1

        chickennuggets = zutatenManager.chickennuggets
        chickennuggets.istVorhanden = 1

        reis = zutatenManager.reis
        reis.istVorhanden = -1

        gericht0 = Essen.Essen("testEssen", 5, 3, 2, 1, [zutatenManager.mehl, zutatenManager.milch], "sdf", "ja", "ja", "-")
        gericht1 = Essen.Essen("testEssen1", 5, 3, 2, 1, [zutatenManager.kartoffeln, zutatenManager.eier], "sdf", "ja", "ja", "-")
        gericht2 = Essen.Essen("testEssen2", 5, 3, 2, 1, [zutatenManager.reis, zutatenManager.chickennuggets], "sdf", "ja", "ja", "-")

        assert MDA.canEssenBeMade(gericht0) == False
        assert MDA.canEssenBeMade(gericht1) == False
        assert MDA.canEssenBeMade(gericht2) == False

    def test_evaluation_zutat_missing(self):
        MDA = mainAI.MamaDooAi()

        zutatenManager = MDA.zutatenManager

        zutatenManager.eier.istVorhanden = -1

        gericht0 = Essen.Essen("testEssen", 5, 3, 2, 1, [zutatenManager.mehl, zutatenManager.milch], "sdf", "ja", "ja", "-")
        gericht1 = Essen.Essen("testEssen1", 5, 3, 2, 1, [zutatenManager.kartoffeln, zutatenManager.eier], "sdf", "ja", "ja", "-")
        gericht2 = Essen.Essen("testEssen2", 5, 3, 2, 1, [zutatenManager.reis, zutatenManager.chickennuggets], "sdf", "ja", "ja", "-")

        MDA.alleGerichte = [gericht0, gericht1, gericht2]

        results = MDA.evaluate()

        assert len(results) == 2
        assert not gericht1 in results

    def test_evaluation_invalid_zutat(self):

        MDA = mainAI.MamaDooAi()

        zutatenManager = MDA.zutatenManager

        zutatenManager.eier.istVorhanden = -1

        gericht0 = Essen.Essen("testEssen", 5, 3, 2, 1, ["hallo", zutatenManager.milch], "sdf", "ja", "ja", "-")
        gericht1 = Essen.Essen("testEssen1", 5, 3, 2, 1, ["moin", zutatenManager.eier], "sdf", "ja", "ja", "-")
        gericht2 = Essen.Essen("testEssen2", 5, 3, 2, 1, ["fufu", zutatenManager.chickennuggets], "sdf", "ja", "ja", "-")

        MDA.alleGerichte = [gericht0, gericht1, gericht2]
        try:
            results = MDA.evaluate()
            assert False
        except AttributeError:
            assert True

        # gericht hat zu viele zutaten
        # gericht hat zu wenige zutaten
        # gericht hat zutaten die nicht vorhanden sind
        pass

    def test_evaluation_no_zutaten_angegeben(self):
        MDA = mainAI.MamaDooAi()

        zutatenManager = MDA.zutatenManager

        zutatenManager.eier.istVorhanden = -1

        gericht0 = Essen.Essen("testEssen", 5, 3, 2, 1, [], "sdf", "ja", "ja", "-")
        gericht1 = Essen.Essen("testEssen1", 5, 3, 2, 1, [zutatenManager.eier], "sdf", "ja", "ja", "-")
        gericht2 = Essen.Essen("testEssen2", 5, 3, 2, 1, [zutatenManager.chickennuggets], "sdf", "ja", "ja", "-")

        MDA.alleGerichte = [gericht0, gericht1, gericht2]
        results = MDA.evaluate()
        assert len(results) == 2

    def test_valid_gericht_no_filters(self):
        MDA = mainAI.MamaDooAi()

        zutatenManager = MDA.zutatenManager

        zutatenManager.wasser.istVorhanden = -1

        gericht0 = Essen.Essen("testEssen", 5, 3, 2, 1, [zutatenManager.milch], "sdf", "ja", "ja", "-")
        gericht1 = Essen.Essen("testEssen1", 5, 3, 2, 1, [zutatenManager.eier], "sdf", "ja", "ja", "-")
        gericht2 = Essen.Essen("testEssen2", 5, 3, 2, 1, [zutatenManager.chickennuggets], "sdf", "ja", "ja", "-")

        MDA.alleGerichte = [gericht0, gericht1, gericht2]
        assert len(MDA.evaluate()) == 3

    def test_valid_gericht_sorted_by_rating(self):
        MDA = mainAI.MamaDooAi()

        zutatenManager = MDA.zutatenManager

        zutatenManager.eier.istVorhanden = -1

        gericht0 = Essen.Essen("testEssen", 3, 10, 10, 10, [zutatenManager.milch], "sdf", "ja", "ja", "-")
        gericht1 = Essen.Essen("testEssen1", 5, 3, 2, 1, [zutatenManager.eier], "sdf", "ja", "ja", "-")
        gericht2 = Essen.Essen("testEssen2", 5, 0, 0, 0, [zutatenManager.chickennuggets], "sdf", "ja", "ja", "-")
        gericht3 = Essen.Essen("testEssen3", 9, 10, 10, 10, [zutatenManager.chickennuggets], "sdf", "ja", "ja", "-")

        gericht4 = Essen.Essen("testEssen4", 10, 3, 2, 1, [zutatenManager.chickennuggets], "sdf", "ja", "ja", "-")

        MDA.alleGerichte = [gericht0, gericht1, gericht2, gericht3, gericht4]
        results = MDA.evaluate(sortedByRating=True)
        assert len(results) == 4
        assert results[0] == gericht4
        assert results[1] == gericht3
        assert results[2] == gericht2
        assert results[3] == gericht0

    def test_valid_gericht_sorted_by_mama(self):
        MDA = mainAI.MamaDooAi()

        zutatenManager = MDA.zutatenManager

        zutatenManager.eier.istVorhanden = -1

        gericht0 = Essen.Essen("testEssen", 8, 10, 10, 10, [zutatenManager.milch], "sdf", "nein", "nein", "-")
        gericht1 = Essen.Essen("testEssen1", 5, 3, 2, 1, [zutatenManager.eier], "sdf", "nein", "nein", "-")
        gericht2 = Essen.Essen("testEssen2", 5, 0, 0, 0, [zutatenManager.chickennuggets], "sdf", "ja", "ja", "-")
        gericht3 = Essen.Essen("testEssen3", 9, 10, 10, 10, [zutatenManager.chickennuggets], "sdf", "nein", "nein", "-")

        gericht4 = Essen.Essen("testEssen4", 10, 10, 10, 10, [zutatenManager.chickennuggets], "sdf", "ja", "ja", "-")

        MDA.alleGerichte = [gericht0, gericht1, gericht2, gericht3, gericht4]
        results = MDA.evaluate(MamaBenötigtFilter=True)
        assert len(results) == 2
        assert results[0] == gericht3
        assert results[1] == gericht0

    def test_valid_gericht_sorted_by_satt(self):
        pass

    def test_valid_gericht_sorted_by_difficulty(self):
        pass

    def test_valid_gericht_sorted_by_gesund(self):
        pass

    def test_valid_gericht_mit_loswerde_bonus(self):
        pass

    def test_gericht_mit_loswerde_bonus_aber_loswerde_bonus_zutat_ist_nicht_vorhanden(self):
        pass

    def test_gericht_evaluation_of_multiple_filters_active(self):
        pass
