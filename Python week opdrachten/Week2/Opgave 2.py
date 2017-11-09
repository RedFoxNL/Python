# a) Dit veranderd de waarde red in blue
d = {"red": 4, "blue": 1, "green": 14, "yellow": 2}
d['red'] = d['blue']
print("a)")
print(d)

# b) Dit geeft de key blue de value + 10 op de huidige value
d = {"red": 4, "blue": 1, "green": 14, "yellow": 2}
d['blue'] += 10
print("b)")
print(d)

# c) Dit geeft de key yellow, de value met de waarde van de lengte van de dictionary
d = {"red": 4, "blue": 1, "green": 14, "yellow": 2}
d['yellow'] = len(d)
print("c)")
print(d)

# d) Dit veranderd de value van green naar orange : 6
d = {"red": 4, "blue": 1, "green": 14, "yellow": 2}
d['green'] = {'orange' : 6}
print("d)")
print(d)

# e) Dit verandert elke value van elke key naar 0
d = {"red": 4, "blue": 1, "green": 14, "yellow": 2}
d = dict.fromkeys(d, 0)
print("e)")
print(d)

# f) Dit verandert niets, want black zat niet in de dictionary
d = {"red": 4, "blue": 1, "green": 14, "yellow": 2}
d.pop('black', None)
print("f)")
print(d)

# g) Hij krijgt de key / value niet, omdat Black niet in de dictionary staat
d = {"red": 4, "blue": 1, "green": 14, "yellow": 2}
d.get('black', None)
print("g)")
print(d)

# h) Black wordt toegevoegd aan de dictionary
d = {"red": 4, "blue": 1, "green": 14, "yellow": 2}
d.setdefault('black', None)
print("h)")
print(d)

# i) Dit maakt van d een nieuwe lege dictionary
d = {"red": 4, "blue": 1, "green": 14, "yellow": 2}
d = {}
print("i)")
print(d)