blue='greenpark picadilly coventgarden holborn russellsquare kingscross'
yellow='towerhill bakerstreet holborn blackfriars temple'
red='bank holborn oxford bondstreet marblearch'
brown='bakerstreet oxford picadilly charingcross'
lines_london = [blue, yellow, red, brown]

# (a)
blue= (blue.split(" "))
yellow= (yellow.split(" "))
red= (red.split(" "))
brown= (brown.split(" "))

set_of_stations = blue, yellow, red, brown

#print(set_of_stations)

# (b)
dict_of_stations = {}
for stations in set_of_stations:
    for stops in stations:
        dict_of_stations[stops] = stations
print(dict_of_stations)

# (c)
print(max(dict_of_stations.keys()) ,max(dict_of_stations.values()))


    