antwoorden = open("antwoord.txt", "r+")
introductietekst ="Welkom bij de vragenlijst over hoe leidinggevende communiceren met hun werknemers. U wordt doorgestuurd naar de eerste vraag. Heel veel succes."

#------------------------------------------------------------------------------------------------
#Inleiding van de vragenlijst
print(introductietekst)
#-------------------------------------------------------------------------------------------------

# Demografische vragen
demografisch = ['Wat is uw geslacht?', 'Wat is uw leeftijd?', 'Wat voor werk doet u?']
antwoorden.write("Demografische vragen \n")
for vraag in demografisch:
    antwoord = input(vraag)
    print("\n")
    antwoorden.write("vraag " + " " + antwoord + "\n")

limit = 1

#Een functie die de schaalvragen afhandelt. Wanneer helemaal eens of eens het antwoord is, wordt de doorvraag gesteld.
def schaalvraag(limit, ja, nee):
    antwoord = input(vragenlijst[limit])
    print("\n")
    antwoorden.write("Vraag " + str(limit) + " " + antwoord + "\n")
    if antwoord == "helemaal eens" or antwoord == "eens":
        antwoord = input(ja)
        print("\n")
        antwoorden.write("Schaalvraag " + str(limit) + " " + antwoord + "\n")
    if antwoord == "helemaal oneens" or antwoord == "oneens":
        antwoord = input(nee)
        print("\n")
        antwoorden.write("Doorvraag " + str(limit) + " " + antwoord + "\n")


#Een functie die de doorvragen afhandelt. Wanneer ja of nee het antwoord is, wordt de doorvraag gesteld.
def doorvraag(limit, ja, nee):
    antwoord = input(vragenlijst[limit])
    print("\n")
    antwoorden.write("Vraag " + str(limit) + " " + antwoord + "\n")
    if antwoord == "ja":
        antwoord = input(ja)
        print("\n")
        antwoorden.write("Doorvraag " + str(limit) + " " + antwoord + "\n")
    if antwoord == "nee":
        antwoord = input(nee)
        print("\n")
        antwoorden.write("Doorvraag " + str(limit) + " " + antwoord + "\n")

#Een functie die de normale openvragen afhandelt.
def vraag(limit):
    antwoord = input(vragenlijst[limit])
    print("\n")
    antwoorden.write("Vraag " + str(limit) + " " + antwoord + "\n")

def einde():
    antwoorden.write("Einde vragenlijst \n")
    antwoorden.write("------------------------------------------------------------------------")
    print("Dit is het einde van de vragenlijst. Hartelijk dank voor het invullen")
    antwoorden.close()

#Vragenlijst is een dictionary met de vragen die gebruikt worden in deze vragenlijst
vragenlijst = {
    1: "Op het moment dat een werknemer een probleem ervaart tijdens het werk, bij wie kan hij/zij het probleem melden?",
    2: "Welke stappen worden er ondernomen bij medewerkers die niet volledig functioneren?",
    3: "Wat wordt er gedaan met medewerkers die slecht presteren?",
    4: "Alle werknemers worden op een gelijke manier behandeld.",
    5: "Hoevaak is er binnen uw bedrijf een functioneringsgesprek?",
    6: "Op welke wijze wordt dit gehanteerd?",
    7: "Welke protocollen gelden bij een ziekmelding?",
    8: "Gelden er duidelijke instructies voor uw medewerkers?",
    9: "Het is belangrijk dat wat er verteld wordt, waar is",
    10: "De boodschap van werkgever naar werknemer moet kort en bondig zijn.",
    11: "Wanneer begrijpt de werknemer wat er bedoelt wordt met de boodschap die wordt overgebracht?",
    12: "De boodschap bevat alleen zakelijke aspecten.",
    13: "De boodschap bevat expressieve aspecten. (hoe we willen overkomen op de ander, voorbeeld:  door kledingstijl, lichaamstaal, praten met of zonder accent)",
    14: "De boodschap bevat relationele aspecten.",
    15: "De boodschap bevat appellerende aspecten. ( invloed die de leidinggevende uitoefent op de werknemer)",
    16: "Werknemers weten wat er van hun verwacht wordt.",
    17: "Welke verschillende communicatie technieken worden er binnen uw bedrijf gehanteerd?",
    18: "Er wordt zelden feedback gegeven tijdens een gesprek.",
    19: "Een belangrijk aspect binnen communicatie is lichaamshouding.",
    20: "De werknemers voelen zich vertrouwd om zijn/haar verhaal te kunnen vertellen.",
    21: "Werknemers voelen zich gehoord binnen het bedrijf",
    22: "Op welke wijze worden uw werknemers gemotiveerd?",
    23: "Taakgericht werken vinden wij een belangrijker aspect dan mensgericht werken."}

#Deelconstruct 1 Persoonlijke aandacht
# Vragen 1
vraag(limit)
limit += 1

# Vraag 2
vraag(limit)
limit += 1

# Vraag 3
vraag(limit)
limit += 1

# Vraag 4 met doorvraag
print("Deze vraag dient met ja of nee beantwoordt te worden")
doorvraag(limit, "Waarom is het belangrijk om alle werknemers gelijk te behandelen",
          "Wat is de reden dat niet alle werknemers gelijk worden behandeld?")
limit += 1

# Vragen 5
vraag(limit)
limit += 1

# Vraag 6
vraag(limit)
limit += 1

# vraag 7
vraag(limit)
limit += 1

# vraag 8
print("Deze vraag dient met ja of nee beantwoordt te worden")
doorvraag(limit, "Op welke manier worden deze vormgegeven?", "Welke andere oplossing is hiervoor bedacht?")
limit += 1

#Deelconstruct 2 De boodschap die wordt overgebracht
# vraag 9
print("Deze vraag dient met ja of nee beantwoordt te worden")
doorvraag(limit,
          "Waarom is het binnen uw bedrijf belangrijk om eerlijk te zijn met de boodschap die wordt overgebracht?",
          "Waarom is het binnen uw bedrijf niet belangrijk om eerlijk te zijn met de boodschap die wordt overgebracht?")
limit += 1

# vraag 10
print("Deze vraag dient met ja of nee beantwoordt te worden")
doorvraag(limit, "Wat is de reden dat de boodschap kort en bondig moet zijn?",
          "Hoe ziet voor u een boodschap eruit die u wil overbrengen?")
limit += 1

# vraag 11
vraag(limit)
limit += 1

# vraag 12
print("Deze vraag dient met ja of nee beantwoordt te worden")
doorvraag(limit, "Welke zakelijke aspecten worden hiermee bedoelt?",
          "Welke aspecten wordt er binnen uw boodschap gehanteerd?")
limit += 1

# vraag 13
print("Deze vraag dient met ja of nee beantwoordt te worden")
doorvraag(limit, "Welke expressieve aspecten worden hiermee bedoelt?",
          "Waarom bevat de boodschap geen expressieve aspecten?")
limit += 1

# vraag 14
print("Deze vraag dient met ja of nee beantwoordt te worden")
doorvraag(limit, "Welke relationele aspecten worden hiermee bedoelt?",
          "Waarom bevat de boodschap geen relationele aspecten?")
limit += 1

# vraag 15
print("Deze vraag dient met ja of nee beantwoordt te worden")
doorvraag(limit, "Welke appellerende aspecten worden hiermee bedoelt?",
          "Waarom bevat de boodschap geen appellerende aspecten?")
limit += 1

# vraag 16
print("Deze vraag dient met ja of nee beantwoordt te worden")
doorvraag(limit, "Hoe zorgt u hiervoor?", "Wat zou een oplossing hiervoor kunnen zijn volgens u?")
limit += 1

#Deelconstruct 3 Communicatie technieken
# vraag 17
vraag(limit)
limit += 1

# vraag 18
print("Deze vraag dient beantwoordt te worden met: helemaal eens, eens, oneens of helemaal oneens")
schaalvraag(limit, "Waarom wordt er zelden feedback gegeven tijdens een gesprek?",
            "Waarom vindt u het wel belangrijk dat er feedback wordt gegeven tijdens een gesprek?")
limit += 1

# vraag 19
vraag(limit)
limit += 1

# vraag 20
print("Deze vraag dient beantwoordt te worden met: helemaal eens, eens, oneens of helemaal oneens")
schaalvraag(limit, "Waaraan merkt u dat?",
            "Wat is de reden dat werknemers zich niet vertrouwd voelen om zijn/haar verhaal te kunnen vertellen?")
limit += 1

# vraag 21
print("Deze vraag dient beantwoordt te worden met: helemaal eens, eens, oneens of helemaal oneens")
schaalvraag(limit, "Hoe zorgt u ervoor dat de werknemers zich gehoord voelen?",
            "Waarom voelen werknemers zich niet gehoord binnen het bedrijf?")
limit += 1

# vraag 22
vraag(limit)
limit += 1

# vraag 23
print("Deze vraag dient met ja of nee beantwoordt te worden")
doorvraag(limit, "Waarom vindt u taakgericht werken een belangrijker aspect?",
          "Waarom vindt u taakgericht werken een minder belangrijk aspect?")
limit += 1

einde()