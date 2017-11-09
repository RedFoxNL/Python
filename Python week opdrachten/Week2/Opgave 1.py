# a) Tuples maken. Resultaat: (1, 2, 3, 4, 5) en (5, ).
tuple11 = (1,2,3,4,5)
print(tuple11)
print(tuple11[4:5])

# b) Tuple uitpakken.
tup = ('xx', 'yy', 'zz')
print(tup[1])

# c) Waarden toevoegen. (tuples kunnen niet gemuteerd worden, dus moet er een nieuwe tuple aangemaakt worden
tup1 = (4, 6, 2, 8, 3, 1)
tup1_2 = (4,6,100,2,8,3,1)
print(tup1_2)

# d) Van tuple naar string.
tup2 = ('a', 'b', 'c')
string = ''.join(tup2)
print(string)

# e) Van list naar tuple.
L = [5, 10, 7]
tuppie = tuple(L)
print(tuppie)

# f) Een lijst van tuples naar individuele lijsten (via zip).
L = [(1,2), (3,4), (8,9)]
test = [(1,1), (2,2), (3,3)]
print(list(zip(*L)))

# g) Van een lijst van tuples naar een dictionary.
L = [ ("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("y", 3) ]
d = {}
for a,b in L:
    d.setdefault(a, []).append(b)
print(d)



