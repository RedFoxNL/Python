# Gemiddelde temperaturen over een bepaalde tijd
NUMBER_OF_DAYS = 10
NUMBER_OF_HOURS = 24
stdinf = open('station_vl.txt','r')

data = []

for i in range(NUMBER_OF_DAYS):
    data.append([])
    for j in range(NUMBER_OF_HOURS):
        data[i].append([])

# read input using input redirection from a file
for line in stdinf:
    if line[0] == '#':
        continue
    L = line.strip().split()
    dag = int(L[0])
    uur = int(L[1])
    temp = int(L[2])
    data[dag - 1][uur - 1] = temp

print("Gemiddelde temperaturen: ")
# find the average daily temperature
for i in range(NUMBER_OF_DAYS):
    dagelijks_temperatuur = 0
    for y in range(NUMBER_OF_HOURS):
        dagelijks_temperatuur += data[i][y]
    print("dag{0:>2} : {1:.1f}".format(i+1, dagelijks_temperatuur / NUMBER_OF_HOURS))