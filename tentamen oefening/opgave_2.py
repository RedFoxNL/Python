'''
statistics.minutes delayed.weather: number of minutes delayed (per month) caused by significant meteorological
conditions that, in the judgment of the carrier, delays or prevents the operation of a flight.
'''

import json
from pprint import pprint

# A
with open('airports.json', 'r') as infile:
    list_of_airports = json.load(infile)
    pprint(list_of_airports)

#B
list_of_delays = ()
for airports in list_of_airports:
    for airports['minutes delayed'] in airports['statistics']:
        print(airports['minutes delayed'])
        list_of_delays += airports.flight , airports.delayed

# sort airports by min_delayed_weather

# #C
# for airports in list_of_delays:
#     print(max(airports[0])), max(airports[1])
#