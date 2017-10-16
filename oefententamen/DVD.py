class objecten:
    #Constructor van de Super klasse Objecten
    def __init__(self, title, gerne, duration, cost):
        self.title = title
        self.gerne = gerne + " Genre "
        self.duration = duration
        self.cost = cost

    #Een functie die de minuten omzet naar uren, afgerond naar 2 decimale getallen achter de komma.
    def mintohour(self):
        duration = int(self.duration) / 60
        return(round(duration,2))

    #De representatie functie, om alle waarden om te zetten in 1 string
    def __repr__(self):
        return 'Objecten: %s, %s, %s, %s' %  (self.title, self.gerne, self.mintohour(), self.cost)

class DVD (objecten):

    #Constructor van de subklasse DVD met de overerfing van de super klasse Objecten.
    #Op de eerste regel geef je aan welke waardes deze klass moet ontvangen, op de 2e regel geef je aan welke hij mag overerfen.
    #Op de derde regel komen de variabelen die nog niet gedeclareerd zijn, welke variabele dus nieuw is in deze klasse.
    def __init__(self, title, gerne, duration, cost,scenes):
        super().__init__(title, gerne, duration, cost )
        self.scenes = scenes

    #Representatie van alles waardes naar 1 string.
    def __repr__(self):
       return 'DVD: %s, %s, %s, %s, %s' %  (self.title,self.gerne, self.mintohour(), self.cost, self.scenes)

class CD (objecten):

    # Constructor van de subklasse DVD met de overerfing van de super klasse Objecten.
    # Op de eerste regel geef je aan welke waardes deze klass moet ontvangen, op de 2e regel geef je aan welke hij mag overerfen.
    # Op de derde regel komen de variabelen die nog niet gedeclareerd zijn, welke variabele dus nieuw is in deze klasse.
    def __init__(self, title, gerne, duration, numbers, cost):
        super().__init__(title, gerne, duration, cost)
        self.numbers = numbers

    # Representatie van alles waardes naar 1 string.
    def __repr__(self):
       return 'CD: %s, %s, %s, %s, %s' % (self.title, self.gerne, self.mintohour(), self.cost, self.numbers)


lijst = []
lijst.append(DVD("Golden Eye", "Actie", 160, 12, 24.95))
lijst.append(CD("Wandering", "Blues", 128, 8, 19.95))
lijst.append(DVD("Kungfo Panda","Humor", 120, 12, 9.95))
lijst.append(objecten("Wondering in bewteen", "Muziek", 128, 15))
for ob in lijst:
    print(ob)