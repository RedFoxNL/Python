# Gevoelstemperatuur programma met de berekening van celcius en beaufort

celcius = int(input("Geef de temperatuur in Celsius: "))
beaufort = int(input("Geef de windkracht: "))
b = beaufort**0.24
g_temp = 13 + (0.62 * celcius) - (14 * b) + (0.47 * celcius * b)
print("De gevoeldstemperatuur is {0:2.1f}".format(g_temp))