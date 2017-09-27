#Library voor input importeren
import sys

# Functie om de lijsten te printen. Gebasseerd op de meegegeven variabele, waarin aangegeven wordt welke lijst gelezen moet worden
def print_Lijst(arg):
    for items in arg:
        print(items)

#Main functie die de basis stappen doet en de functies: lasten en Hobby aanroept en verwerkt
def main(inkomen, inkomen2):
    inkomen = int(inkomen) + int(inkomen2)
    lastenV = lasten()
    print(lastenV)
    hobbyV = hobby()
    print(hobbyV)
    vrijeRuimte = inkomen - lastenV - hobbyV
    print('De besteden budget bedraagt: €', int(vrijeRuimte))

#Functie Lasten omschrijft alle lasten in een dictionary, die in een return opgevraagd kunnen worden
def lasten():
    totaalLasten = 0
    lasten = {'zorg':130, 'school': 350, 'Mobiel':31, 'Sportschool':25}
    zien = input('Wilt u de lijst met lasten zien?')
    if zien == 'ja':
        print_Lijst(lasten)
        antwoord = input('Zijn er nog lasten die toegevoegd moeten worden?')
        if antwoord == 'ja':
            last = input('Welke is dit?')
            last2 = input('hoeveel bedraagt deze last?')
            lasten[last] = last2
            for e in lasten.values():
                totaalLasten += int(e)
                print(totaalLasten)
        else:
            for e in lasten.values():
                totaalLasten += int(e)
                print(totaalLasten)
    return int(totaalLasten)

#Functie Hobby omschrijft alle lasten in een dictionary, die in een return opgevraagd kunnen worden.
def hobby():
    hobby = {'Bezine kosten':200, 'horloges':100}
    totaalHobby = 0
    print_Lijst(hobby)
    antwoordHobby = input("Zijn er nog hobby's die toegevoegd moeten worden?")
    if antwoordHobby == 'ja':
        hobbyLast = input('welke is dit?')
        hobbyLast2 = input('Wat bedraagt deze hobby?')
        hobby[hobbyLast] = hobbyLast2
        for i in hobby.values():
            totaalHobby += int(i)
            print(totaalHobby)
    else:
        for i in hobby.values():
            totaalHobby += int(i)
            print(totaalHobby)
    return int(totaalHobby)

#Hier wordt de functie main aangeroepen met 2 soorten inkomen als variabelen
main(950, 89)