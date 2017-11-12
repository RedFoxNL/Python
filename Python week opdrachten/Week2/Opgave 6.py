import string, sys
# a) Schrijf een functie unique_list(L), die teruggeeft een lijst met alle unieke elementen van L.
#    Voorbeeld: L = [1,2,3,3,3,3,4,5] dan geeft print(unique_list(L)) als resultaat: [1, 2, 3, 4, 5].

def unique_list(L):
    s = set(L)
    return s

# b) Schrijf een functie even_elements (L), die teruggeeft een lijst met alle even elementen van L.
#    Voorbeeld: L = [1, 2, 3, 4, 5, 6, 7, 8, 9] dan geeft print(evene_elements(L)) als resultaat: [2, 4, 6, 8].

def even_elements(L):
    s = []
    for x in L:
        if x % 2 == 0:
            s.append(x)
    return s

# c) Schrijf een functie is_pangram(str) die teruggeeft of de string str een pangram is. Een pangram is een woord of
#    zin dat elke letter van het alfabet (tenminste een keer) bevat.
#    Voorbeeld: str= "Filmquiz bracht knappe ex-yogi van de wijs". Print(is_pangram(str)) geeft True.
#    Tip : string.ascii_lowercase geeft een string met alle letters van het alfabet.

def is_pangram(str):
    alphaset = set(string.ascii_lowercase)
    return alphaset <= set(str.lower())

# d) Schrijf een functie sd(dict) die teruggeeft een gesorteerde lijst met paren (key, value).
#    Voorbeeld: dict = {'ed': 5, 'carl':3, 'alan':1, 'bob':2, 'dan':4}
#    print(sd(dict)) geeft als resultaat [('alan', 1), ('bob', 2), ('carl', 3), ('dan', 4), ('ed', 5)]
#    Dit kan je eenvoudig oplossen via sorted(dict.items()), maar doe dit ook door een ananieme functie mee te
#    geven, dus met key=lambda.

def sd(dict):
    # return sorted(dict.items())
    return sorted(dict.items(), key=lambda x: x[1])


#----------------------------------------------------------

# a) uitkomst opdracht a
L = [1,2,3,3,3,3,4,5]
print(unique_list(L))

# b) uitkomst opdracht b
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even_elements(L))

# c) uitkomst opdracht c
print(is_pangram("Filmquiz bracht knappe ex-yogi van de wijs"))

# d) Uitkomst opdracht d
dict = {'ed': 5, 'carl':3, 'alan':1, 'bob':2, 'dan':4}
print(sd(dict))