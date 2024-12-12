import math
import numpy as np
import re

## Fetch data
def Create_Data(day = 0, test = False):
    if test:
        file = f"Day{day}_test.txt"
    else:
        file = f"Day{day}.txt"

    raw = []
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            buffer = []
            for element in line:
                buffer.append(int(element))
            raw.append(buffer)

    return raw
def Point_Exists(data, idx, idy):
    if ((0 <= idx < len(data)) and (0 <= idy < len(data[idx]))):
        return True
    else:
        return False


## Solutions
summited = []
def step(data, x, y, path=0, first=True, unique=True):
    global summited
    directions = {"U": {"x": x, "y": y-1}, "D": {"x": x, "y": y+1}, "L": {"x": x-1, "y": y}, "R": {"x": x+1, "y": y}}

    if(data[y][x]==9):
        if unique:
            if([x,y] not in summited):
                summited.append([x,y])
        else:
            summited.append([x,y])

    retval = False
    for dir, coords in directions.items():
        if( Point_Exists(data, coords["x"], coords["y"]) ):
            
            if((data[coords["y"]][coords["x"]] - data[y][x] == 1)):
                #print(path, ":", x, y, data[y][x])

                step(data, coords["x"], coords["y"], path+1, False, unique)

                data[y][x] == 8 and data[coords["y"]][coords["x"]] == 9
            else:
                pass
        else:
            pass


# == Part One
def Part_One(data):
    global summited

    zero_points= []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if(data[y][x] == 0):
                zero_points.append([x,y])

    result = 0
    for point in zero_points:
        tx = point[0]
        ty = point[1]
        step(data, tx, ty)
        result += len(summited)
        summited = []

    return result

# == Part Two
def Part_Two(data):
    global summited

    zero_points= []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if(data[y][x] == 0):
                zero_points.append([x,y])

    result = 0
    for point in zero_points:
        tx = point[0]
        ty = point[1]
        step(data, tx, ty, unique=False)
        result += len(summited)
        summited = []

    return result


data = Create_Data(day = 10, test = False)

print("Part One:", Part_One(data))

print("Part Two:", Part_Two(data))
