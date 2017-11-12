blue ='greenpark picadilly coventgarden holborn russellsquare kingscross'
yellow ='towerhill bakerstreet holborn blackfriars temple'
red ='bank holborn oxford bondstreet marblearch'
brown ='bakerstreet oxford picadilly charingcross'
lines_london = [blue, yellow, red, brown]


# (a)
set_of_stations = set()
for line in lines_london:
    station = line.split()
    for s in station:
        set_of_stations.add(s)


print(set_of_stations)

# (b)
dict_of_stations = {}
for s in set_of_stations:
    neighbors = []
    for line in lines_london:
        stations = line.split()
        if s in line:
            i = stations.index(s)
            if i > 0:
                neighbors.append(stations[i-1])
            if i < len(lines_london) -1:
                neighbors.append(stations[i+1])
    dict_of_stations[s] = neighbors

for k,v in dict_of_stations.items():
    print(k,v)


# (c)
print('station met de meeste buren:', max(dict_of_stations, key=lambda k:len(dict_of_stations[k])))
