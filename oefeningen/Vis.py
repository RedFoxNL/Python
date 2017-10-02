# Dit programma gaat over vissen in een aquarium.

def main(id, soort, gewicht, lengte, kleur):
    id = id
    soort = soort
    gewicht = gewicht
    lengte = lengte
    kleur = kleur

    vis = []
    vis.append(id, soort, gewicht, lengte, kleur)
    print(vis)
    bijten(soort)

# Deze functie gaat na of de vis een bijtende vis is of niet
def bijten(soort):
    bijtVis = ['haaien','piranja','kreeft']
    for vis in bijtVis:
        if soort == bijtVis:
            print("Deze vis mag niet geplaatst worden bij de volgende vissen: ")
            print(vis)
        else:
            vegetarisch(soort)

# Deze functie gaat na of een vis vegetarich is of niet. Zoja, wat eet deze vis?
def vegetarisch(soort):
    vegetarischeVis = {'makreel':1,'garnaal':2,'haring':3}
    soortVis = ['start index op 1',"Deze vis eet alleen plancton", 'Deze vis eet plancton en zeewier','Deze vis eet alleen aardappelen']
    if soort in vegetarischeVis:
        for vis in vegetarischeVis:
            if soort == vis:
                waarde = vegetarischeVis[soort]
                print(soortVis[waarde])


# Deze functie kijkt aan de hand van de meegegeven lengte, welke bak qua maat het beste aansluit op de vis
def aqarium(lengte):
    maat = lengte
    print(maat)
    aqariumBak = {2:"bak 1", 6:"bak 2", 10:"bak 3"}
    while maat not in sorted(aqariumBak):
        maat = maat + 1
    for key, value in aqariumBak.items():
        if maat == key:
            print("De lengte van de vis is geschikt voor", value)



aqarium(5)
vegetarisch('makreel')
