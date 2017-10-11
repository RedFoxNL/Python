# Opdracht Huizen na aanleiding van managers en developers en employees en managers

class Huis:
    huizen = ()

    def __init__(self, grote, prijs, hoe_mensen, tuin):
        self.grote = grote
        self.prijs = prijs
        self.prijs = (self.prijs / 1000)
        self.hoe_mensen = hoe_mensen
        self.tuin = tuin

class Koophuis(Huis):
    koophuis = ()

    def __init__(self, grote, prijs, hoe_mensen, tuin, koophuis):
        super().__init__(grote, prijs, hoe_mensen, tuin)
        self.koophuis = koophuis

class Huurwoning(Huis):
    huurwoning = ()

    def __init__(self, grote, prijs, hoe_mensen, tuin, huurwoning):
        super().__init__(grote, prijs, hoe_mensen, tuin)
        self.huurwoning = huurwoning
        