import math
import numpy as np
import re

## Fetch data
def Create_Data(day = 0, test = False):
    if test:
        file = f"Day{day}_test.txt"
    else:
        file = f"Day{day}.txt"

    with open(file, 'r') as f:
        raw = [line.strip() for line in f]

    return raw

def Process_Data(data):

    id = 0
    string = []
    for num in range(len(data)):
        if num%2 == 0:
            for x in range(int(data[num])):
                string.append(f"{id}")
            id += 1
        else:
            for x in range(int(data[num])):
                string.append(".")

    #print(string)
    return string


## Solutions

# == Part One
def Part_One(data):

    for id in range(len(data)-1, 0-1, -1):

        if(not data[id] == "."):
            first_empty = data.index(".")
        
            if(first_empty > id):
                break
        
            data[first_empty] = data[id]
            data[id] = "."
        else:
            continue

        #print(''.join(data))

    checksum = 0
    for idx, value in enumerate(data):
        if(value == "."):
            break

        checksum += int(idx)*int(value)
        #print(idx, value)
    
    return checksum


def generate_data(data):
    print("regen", data)

    last = data[0]
    '''
    new_data = []
    for char in data:
        if(char == last):
            new_data.append(char)
        else:
            new_data.append(",")
            new_data.append(char)
        last = char
    '''
    comma = []
    for idx, char in enumerate(data):
        if(not char == last):
            comma.append(idx)
        last = char

    for id in comma[::-1]:
        data.insert(id, ',')

    new_data = (''.join(data))
    print("ujrageneralva", new_data)
    print()
    exit()
    return data


# == Part Two
def Part_Two(data):
    new_data = generate_data(data.copy())

    for i in range(len(new_data)-1, 0-1, -1): # not empty
        print (i , "/" , len(new_data)-1, end='\r')
        if('.' in new_data[i]):
            continue

        for o in range(len(new_data)):  # empty spaces
            if (o >= i ):
                break
            if('.' in new_data[o]):
                
                if(len(new_data[i]) <= len(new_data[o])): 

                    if(len(new_data[o]) == len(new_data[i])):
                        new_data[o], new_data[i] = new_data[i], new_data[o]
                    else:
                        placeholder_num = len(new_data[o]) - len(new_data[i])

                        new_data[o], new_data[i] = new_data[i] + ('.' * placeholder_num), new_data[o][:len(new_data[i])]
                    
                    regen_data = []

                    print(new_data)
                    for j in new_data:
                        if('.' in j):
                            for k in j:
                                regen_data.append(k)
                        else:
                            regen_data.append(j)
                    new_data = generate_data(regen_data.copy())
                    break

    #print(''.join(new_data))

    print(new_data)

    checksum = 0
    for idx, value in enumerate(new_data):
        if("." in value):
            continue
        else:
            checksum += int(idx)*int(value)
        #print(idx, value)
    
    return checksum



data = Create_Data(day = 9, test = True)
processed = Process_Data(data[0])

print("Part One:", Part_One(processed.copy()))

print("Part Two:", Part_Two(processed.copy()))
