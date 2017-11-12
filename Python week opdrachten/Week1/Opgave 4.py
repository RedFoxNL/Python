# Samenvoegen, uitlezen en manipuleren van lijsten

L1 = [30, 1, 2, 1, 0]
L2 = [1, 21, 13]

# Print de lijsten achter elkaar uit
print(L1 + L2)

# print 3x L2 uit achter elkaar
print(3 * L2)

# controleert of L1 meer waardes bevat dan L2
print(L1 > L2)

# Comprehension in lijsten
print(x for x in L1)

# Comprehension in lijsten
print(x for x in L1 if x in L2)
