# Convert a length and diameter given in centimeter to inches
import math

price_list = (0.1 , 0.25 , 0.5 , 0.8 , 1.05 , 1.5 , 2.0 , 2.5 , 3.1 , 3.7)

def cm_to_inch(input_cm):
    result = int(input_cm) / 2.54
    return result

def calc_cost_pipe(inch_length , inch_diameter):
    inch_length = inch_length
    inch_diameter = price_list[inch_diameter -1]
    totaal = int(inch_diameter) * inch_length
    print("De totaal prijs komt op €",totaal)
    return totaal

def main():
    #2 statements die gebruikers om decimalen vraagt
    vraag1 = input("Wat is de diameter van de buis in centimeter?")
    vraag2 = input("Wat is de lengte van de buis")

    #eerste print is input en waarde van cm naar inch
    print("De ingevoerde waarde van de diameter", vraag1, ", Dit is de diameter omgerekend", round(cm_to_inch(vraag1)), "inch")

    #tweede print is prijs van de pijp
    calc_cost_pipe(int(vraag1), int(vraag2))

main()

