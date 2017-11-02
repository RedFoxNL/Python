i = 0
packet_list=[]
count = 0
# read file that contains network packets
with open('packet_example.txt', 'r') as f:
    string = ''.join(str(x) for x in f)

while i < len(string)-15:
    MacAdress = ''.join(string[i: i + 12])
    begin = i +12
    size = ''.join(string[begin: begin + 2])
    intSize = int(size,16)
    message = ''.join(string[begin + 2: begin + intSize + 2])
    i += 12 + 2 + intSize

    packet_list.append([MacAdress, intSize ,message])

    pass

for packet in packet_list:
    print(packet)