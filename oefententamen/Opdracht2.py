packets_str = ''
with open('packet_example.txt', 'r') as f:
    packets_str = f.read()

packet_length=0
mac_address =''
packet_content=''
packetstart = 0
packetend = -1

packet_list=[]

# for pointer in range(0,len(packets_str)):
#     if pointer

mac_address = packets_str[0:13]
packet_length = packets_str[13:16]
packet_content = packets_str[17:62]
print("Het mac adres is", mac_address)
print("Packet lengte is",packet_length)
print("Dit is de boodschap", packet_content)

#Nu moet het zo gemaakt worden dat hij de waarden van packet_str zelf uitleest en invoerd etc,
#Totdat de packetleeg is en in packet_list gooit
#daarna kunnen de waarden opnieuw gebruikt worden

for packet in packet_list:
    print(packet)


