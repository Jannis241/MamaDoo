class Manager():
    def __init__(self) -> None:
        self.eier = Zutat("eier")
        self.mehl = Zutat("mehl")
        self.milch = Zutat("milch")
        self.salz = Zutat("salz")
        self.pfeffer = Zutat("pfeffer")
        self.butter = Zutat("butter")
        self.speck = Zutat("speck")
        self.kartoffeln = Zutat("kartoffeln")
        self.zwiebeln = Zutat("zwiebeln")
        self.hähnchenbrustfilet = Zutat("hähnchenbrustfilet")
        self.öl = Zutat("öl")
        self.muskatnuss = Zutat("muskatnuss")
        self.fischstäbchen = Zutat("fischstäbchen")
        self.lachs = Zutat("lachs")
        self.tomatensoße = Zutat("tomatensoße")
        self.käse = Zutat("käse")
        self.salami = Zutat("salami")
        self.schinken = Zutat("schinken")
        self.pilze = Zutat("pilze")
        self.paprika = Zutat("paprika")
        self.oliven = Zutat("oliven")
        self.spaghetti = Zutat("spaghetti")
        self.hackfleisch = Zutat("hackfleisch")
        self.nudeln = Zutat("nudeln")
        self.wraps = Zutat("wraps")
        self.salat = Zutat("salat")
        self.gurken = Zutat("gurken")
        self.mayonnaise = Zutat("mayonnaise")
        self.reis = Zutat("reis")
        self.bürgerbrötchen = Zutat("bürgerbrötchen")
        self.ketchup = Zutat("ketchup")
        self.salzgurken = Zutat("salzgurken")
        self.zaziki = Zutat("zaziki")
        self.nutella = Zutat("nutella")
        self.vanillezucker = Zutat("vanillezucker")
        self.zimt = Zutat("zimt")
        self.grieß = Zutat("grieß")
        self.pflaumenmus = Zutat("pflaumenmus")
        self.vanille_soße = Zutat("vanille_soße")
        self.gyros = Zutat("gyros")
        self.gyros_fleisch = Zutat("gyros_fleisch")
        self.mören = Zutat("mören")
        self.wurst = Zutat("wurst")
        self.chili_con_carne = Zutat("chili_con_carne")



class Zutat():
    def __init__(self, name) -> None:
        self.name = name
        self.istVorhanden = 0 # 1 will loswerden, 0 habe ich (default), -1 habe ich nicht
        self.isAddOn = False



