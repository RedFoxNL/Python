#Library voor input importeren
import sys

def nettoInkomen(inkomen1, inkomen2='NONE',inkomen3='NONE'):
    inkomen = inkomen1 + inkomen2 + inkomen3
    return inkomen

def lasten():
    totaalLasten = 0
    lasten = {}
    for items in lasten:
        print(items)
        antwoord = input('Zijn er nog lasten die toegevoegd moeten worden?')
        if antwoord == 'ja':
            last = input('Welke is dit?')
            last2 = input('hoeveel bedraagt deze last?')
            lasten.append(last, last2)
            totaalLasten += lasten.values()
        else:
            totaalLasten += lasten.values()
    return totaalLasten

def Hobby():
    totaalHobby = 0
    hobby = {}
    for item in hobby:
        print(item)
        antwoordHobby = input("Zijn er nog hobby's die toegevoegd moeten worden?")
        if antwoordHobby == 'ja':
            hobbyLast = input('welke is dit?')
            hobbyLast2 = input('Wat bedraagt deze hobby?')
            hobby.append(hobbyLast, hobbyLast2)
            totaalHobby += hobby.values()
        else:
            totaalHobby += hobby.values()
    return totaalHobby

def totaal():
    vrijeRuimte = nettoInkomen() - lasten() - Hobby()
    print('De besteden budget bedraagt: €',int(vrijeRuimte))

Hobby()