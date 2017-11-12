import random
#Gegeven lijst L = [30, 1, 2, 1, 0, "hello", "Goodbye"]. Geef aan wat het resultaat is na elke statement (waarbij L na
#elke statement weer is als aan het begin).

L = [30, 1, 2, 1, 0, "hello", "Goodbye"]

# Index geeft de waarde van positie 1
print(L.index(1))

# Count telt de aantal keren dat 1 voorkomt in de lijst
print(L.count(1))

# Len geeft de lengte van de aantal variabelen, maar werkt niet omdat het of INT of String moet zijn en niet beide
#print(len(L))

# Max geeft het hoogste getal weer in een lijst, werkt nu niet omdat er String waardes tussen INT waardes zitten
#print(max(L))

# Append voegt 40 toe aan de lijst
L.append(40)
print(L)

# Insert voegt 43 toe aan positie 1 van de index van de lijst
L.insert(1, 43)
print(L)

# Extend breidt de lijst uit met 1 en 43
L.extend([1, 43])
print(L)

# Remove verwijdert "hello" uit de lijst
L.remove("hello")
print(L)

# Pop verwijdert de laatste toegevoegde waarde uit de lijst
L.pop()
print(L)

# In statement controleerd of de waarde in de lijst zit
if "Goodbye" in L:
    print("Goodbye zit in de lijst")

# Pop verwijdert de waarde uit de lijst met de positie als de positie is meegegeven
L.pop(3)
print(L)

# Sort sorteert de lijst van laag naar hoog, maar dat kan niet in dit geval vanwege String en Int in de lijst
#print(L.sort())

# Random.shuffle verschuift willekeurige de waarden van positie in de lijst
random.shuffle(L)
print(L)
