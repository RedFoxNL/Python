import json
from pprint import pprint

# A
with open('airports.json', 'r') as infile:
    list_of_airports = json.load(infile)
    #pprint(list_of_airports)

#B
list_of_delays = []
for airports in list_of_airports:
    code = airports['airport']['code']
    min_delayed_weather = airports['statistics']['minutes delayed']['weather']
    list_of_delays.append((code, min_delayed_weather))

for e in list_of_delays:
    print(e)

# #C
list_of_delays_sorted = sorted(list_of_delays, key=lambda k: k[1], reverse=True)
for x,y in list_of_delays_sorted:
    print(x,y)
