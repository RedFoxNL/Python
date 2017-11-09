from collections import Counter

# a) Het sorteren van een dictionary
D = {'c':1, 'b':2, 'a':3, 'e':1, 'd':3}
for k in sorted(D.keys()):
    print(k, D[k])

# b) Alleen items met unieke waarden
D = {'a':1, 'b':2, 'c':3, 'd':1, 'e':3}
c = Counter(D.values())
result = {}
for k,v in D.items():
    if c[v] == 1:
        result[k] = v
print(result)

# c) Unieke waarden in een lijst van dictionaries (via een set).
L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
s = set()
for k in L:
    for v in k.values():
        s.add(v)
print(s)

# D) Tel waarden met hetzelfde key bij elkaar op
L = [{'a':1, 'b':2, 'c':3},{'a':5,'b':4,'c':2}]
result = Counter()
for d in L:
    result = result + Counter(d)
print(result)

# e) twee lijsten samenvoegen naar een dict (via zip).
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)
