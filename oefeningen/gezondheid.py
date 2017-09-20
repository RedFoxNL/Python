class mensen:
    def __init__(self,  lengte, gewicht, leeftijd):
        self.lengte = lengte
        self.gewicht = gewicht
        self.leeftijd = leeftijd

    def print_Persoon(self):
        print("""
        lengte: {} cm
        Gewicht: {} kg
        Leeftijd: {}""".format(self.lengte, self.gewicht, self.leeftijd))

class vrouw (mensen):
    def meisje(self,  geslacht):
        geslacht = geslacht
        vrouw = 'vrouw'
        if geslacht == vrouw:
            if self.gewicht > 45 and self.gewicht < 80:
                if self.lengte > 150 and self.lengte < 180:
                    if self.leeftijd > 18 and self.leeftijd < 35:
                        print("De vrouw is gezond")
                    else:
                        print("De leeftijd is niet in verhouding met de lengte")
                else:
                    print("Het gewicht is niet in verhouding met de lengte")
            else:
                print("De vrouw is te zwaar")
        else:
            print("Er moet een vrouw ingevoerd worden")

class man (mensen):
    def jongen(self, geslacht):
        geslacht = geslacht
        man = 'man'
        if geslacht == man:
            if self.gewicht > 75 and self.gewicht < 110:
                if self.lengte > 175 and self.lengte < 195:
                    if self.leeftijd > 18 and self.leeftijd < 35:
                        print("De man is gezond")
                    else:
                        print("De leeftijd is niet in verhouding met de lengte")
                else:
                    print("Het gewicht is niet in verhouding met de lengte")
            else:
                print("De man is te zwaar")
        else:
            print("Er moet een man ingevoerd worden")

persoon = mensen (185, 80, 27)
persoon1 = mensen (160, 60, 27)
persoon.print_Persoon()
persoon1.print_Persoon()
print("\n")

man.jongen(persoon, 'man')
vrouw.meisje(persoon1, 'vrouw')