import json
from pprint import pprint
cnt = 0
var = 0

#openen van de JSON file
with open('books.json', 'r') as infile:
    book_list = json.load(infile)

#van elk boek een aparte dictionary maken
#cnt houdt bij hoeveel boeken de maakt woorden in book_list
#var telt alle prijzen bij elkaar
for book in book_list:
    var += (book["price"])
    cnt += 1

#de opgetelde bedragen var, delen door de opgetelde boeken cnt, afgerond op 2 decimalen na de komma.
gemiddelde =round(var / cnt, 2)
print ("Gemiddelde prijs is €",gemiddelde)

#functie die de auteur weergeeft van elke boek
def author(book_list):
    return book_list['author']

#boeken gesorteerd op auteur doormiddel van de return van de functie auteur
pprint(sorted(book_list, key=author))


# sorteer alle boeken op achternaam van auteur is helaas niet gelukt