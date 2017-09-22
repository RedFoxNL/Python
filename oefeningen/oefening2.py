import sys

def main():
    counter = 1    counter = 1
    for x in range(1,11):
        GemiddeldePerDag(counter)
        counter += 1


def GemiddeldePerDag(arg):
    counter = arg
    with open('station_VL.txt', 'r') as f:
        maxTemp = 0
        for lines in f:
            l = str.split(lines)
            if l[0] == str(counter):
                maxTemp += int((l[2]))
        maxTemp = str(maxTemp/24)
        dagTemp = maxTemp[0:2]+maxTemp[3:5]
        print('Op dag',counter, 'was het gemiddeld',dagTemp,'graden Celius')

main()