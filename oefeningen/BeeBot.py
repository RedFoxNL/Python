

richting= {"rechts":1, "links":2, "vooruit":3, 'achteruit':4}


richtingg =input("Welke richting moet hij op? ")
hoevaak = input('hoevaak?')

for i in richting.values():
    print(i)
    if richtingg in richting.values():
        print('De beebot gaat ', hoevaak,  i)

