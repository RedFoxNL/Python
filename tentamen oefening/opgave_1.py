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
dict_of_stations = {x: [] for x in set_of_stations}
for line in lines_london:
	last = None
	for station in line.split(' '):
		if last is not None:
			dict_of_stations[last].append(station)
			dict_of_stations[station].append(last)
			last = station
    for k,v in dict_of_stations.items():
    print (k,v)
# (c)
print(max(dict_of_stations.keys()) ,max(dict_of_stations.values()))


    