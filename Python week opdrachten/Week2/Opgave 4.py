
# a) De doorsnede van twee sets en print daarwaar de variabelen overeenkomen uit de verschillende sets.
s1 = {1, 4, 5, 6}
s2 = {1, 3, 6, 7}
print(s1 & s2)

#b) Het symmetrisch verschil van twee sets en print alleen de waarden uit die niet in beide voorkomt.
s3 = {1, 4, 5, 6}
s4 = {1, 3, 6, 7}
print(s3 ^ s4)

#c) De elementen in grote lijst vinden (via set. Zitten 15 en 11 in de lijst? Resultaat: True
L = [1, 7, 4, 8, 9, 9, 4, 1, 4, 11, 14, 21, 15, 5, 2, 5]
l = set(L)
print({15,11} <= l)
