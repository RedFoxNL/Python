# Schrijf een programma dat controleert of een woord een palindroom is

def palingdroom(woord):
    woord = woord
    check = woord[::-1]
    if woord == check:
        print("Het woord is een palindroom")
    else:
        print("Het woord is geen palindroom")

palingdroom('lepel')
palingdroom('test')
palingdroom('parteretrap')