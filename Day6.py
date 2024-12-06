import math
import numpy as np

## Fetch data
file = "Day6.txt"

with open(file, 'r') as f:
    raw = [line.strip() for line in f]

def exists(array, idx, idy):
    if ((0 <= idx < len(array)) and (0 <= idy < len(array[idx]))):
        return True
    else:
        return False

def is_obstructions(array, idx, idy):
    if(array[idy][idx] == "#"):
        return True
    else:
        return False

def find_start(array):
    for line in range(len(array)):
        char = '^'
        if(char in array[line]):
            x = array[line].find("^")
            return [x, line]

seq_count = 0
def next_step(array, x, y, reset=False):
    global seq_count
    if(reset): 
        seq_count = 0
        return

    step_seq = [[x, y-1], [x+1, y], [x, y+1], [x-1, y]] 


    next = step_seq[seq_count%4]
    if(not exists(array, next[0], next[1])):
        return -1
    
    if(is_obstructions(array, next[0], next[1])):
        seq_count += 1
        next = step_seq[seq_count%4]        

    return next


## Solutions
first_run = True
first_positions = []

def Part_One(array, start):
    global first_run, first_positions

    positions = []
    map = [[char for char in line] for line in array]

    #print(np.array(map))

    next = next_step(array, 0,0, reset=True)
    x = start[0]
    y = start[1]

    size = len(array) * len(array[0])

    i = 0
    while(True):
        if (i>size):
            return -1   # Loop

        next = next_step(array, x,y)
        map[y][x] = "X" # DEBUG
        
        if ([x,y] not in positions):
            positions.append([x, y])

        if next == -1:
            break
        
        x = next[0]
        y = next[1]
        i += 1

    #print()
    #print(np.array(map)) #DEBUG
    if first_run:
        first_positions = positions.copy()
        first_run = False

    return sum((''.join(line)).count('X') for line in map)
    


def Part_Two(array,start):
    loop = 0
    for posid in range(len(first_positions)-1, 5, -1):
        print(len(first_positions)-1, posid)
        y = first_positions[posid][1]
        x = first_positions[posid][0]

        map = [[char for char in line] for line in array]
        
        map[y][x] = "#"

        new_map = [''.join(line) for line in map]
        
        if (Part_One(new_map, start) == -1):
            loop += 1

        
    return loop


start = find_start(raw)

print("Part One:", Part_One(raw, start))

print("Part Two:", Part_Two(raw, start))
