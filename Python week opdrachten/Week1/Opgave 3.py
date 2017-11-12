# Positie bepaling van de variabelen in een lijst

L = ['a', 'b', 'c', 'd', 'e']

# Geeft de variabelen aan vanaf index 1 tot 3 indexes terug vanaf het einde. ( ['b'] )
print(L[1 : -3])

# Geeft de variabelen weer vanaf 4 posities van rechts naar links, tot 2 posities van rechts naar links ( ['b', 'c'] )
print(L[-4 : -2])

# Geeft de variabelen weer vanaf index 0 tot index 2( ['a', 'b', 'c'] )
print(L[:3])

# Geeft de variabelen weer vanaf index 0 tot index 1( ['a', 'b'] )
print(L[:2])

# Geeft de variabelen weer van index 0 tot index 1 + vanaf index 2 tot het einde ( ['a', 'b', 'c', 'd', 'e'] )
print(L[:2] + L[2:])

# Geeft de waarden weer vanaf 0 tot de een na laaste waarde uit de lijst ( ['a', 'b', 'c', 'd'] )
print(L[:-1])

# Geeft de variabelen achterstevoren weer ( ['e', 'd', 'c', 'b', 'a'] )
print(L[::-1])

# Print de lijst vanaf het begint tot het einde, geen posities opgegeven ( ['a', 'b', 'c', 'd', 'e'] )
print(L[:])