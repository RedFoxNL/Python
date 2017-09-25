#Library voor input importeren
import sys


inkomen = 1030

totaalLasten = 0
lasten = {}
zien = input('Wilt u de lijst met lasten zien?')
if zien == 'ja':
    # for items in lasten:
    #     print(items)
    antwoord = input('Zijn er nog lasten die toegevoegd moeten worden?')
    if antwoord == 'ja':
        last = input('Welke is dit?')
        last2 = input('hoeveel bedraagt deze last?')
        lasten[last] = last2
        for e in lasten.values():
            totaalLasten += e
    else:
        for e in lasten.values():
            totaalLasten += e

    hobby = {}
    totaalHobby = 0
    for item in hobby:
        print(item)
        antwoordHobby = input("Zijn er nog hobby's die toegevoegd moeten worden?")
        if antwoordHobby == 'ja':
            hobbyLast = input('welke is dit?')
            hobbyLast2 = input('Wat bedraagt deze hobby?')
            hobby[hobbyLast] = hobbyLast2
            for i in hobby.values():
                totaalHobby += i
        else:
            for i in hobby.values():
                totaalHobby += i


    vrijeRuimte = inkomen-100-100
    print('De besteden budget bedraagt: €',int(vrijeRuimte))
