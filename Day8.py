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

def Point_Exists(idx, idy):
    if ((0 <= idx < len(data)) and (0 <= idy < len(data[idx]))):
        return True
    else:
        return False


def Process_Data(data):
    frequencies = []
    antennas = []

    for lineid in range(len(data)):
        for charid in range(len(data[lineid])):
            
            freq = data[lineid][charid]
            x = charid
            y = lineid

            if(data[lineid][charid] == "."):
                continue
            else:
                antennas.append([freq, x, y])

                if(freq not in frequencies):
                    frequencies.append(freq)
                

    return frequencies, antennas
## Solutions

# == Part One
def Part_One(frequencies, all_antennas):

    antinodes = []
    # Iter over frquencies
    for freq in frequencies:
        
        antennas = []
        # find antennas with given frequency
        for antenna in all_antennas:
            if antenna[0] == freq:
                antennas.append(antenna)

        # Check if at least 2 antennas
        if len(antennas) == 1:
            continue

        
        for ant1 in antennas:
            for ant2 in antennas:
                vector = {"x": ant2[1] - ant1[1], "y": ant2[2] - ant1[2]}

                # Skip if ant1 and ant2 are the same antennas
                if(vector["x"] == 0 and vector["y"] == 0):
                    continue
                
                # Antinode coord
                antinodex, antinodey = (ant1[1]-vector["x"], ant1[2]-vector["y"])

                # Check if point in map
                if(Point_Exists(antinodex, antinodey) and [antinodex, antinodey] not in antinodes):
                    antinodes.append([antinodex, antinodey])
                    map[antinodey][antinodex] = "#"
            
            # DEBUG
    #print(str(np.array(map)).replace('\'','').replace('[','').replace(']','').replace(' ',''))
    
    return len(antinodes)

# == Part Two
def Part_Two(frequencies, all_antennas):

    antinodes = []
    # Iter over frquencies
    for freq in frequencies:
        
        antennas = []
        # find antennas with given frequency
        for antenna in all_antennas:
            if antenna[0] == freq:
                antennas.append(antenna)

        # Check if at least 2 antennas
        if len(antennas) == 1:
            continue

        
        for ant1 in antennas:
            for ant2 in antennas:
                vector = {"x": ant2[1] - ant1[1], "y": ant2[2] - ant1[2]}

                # Skip if ant1 and ant2 are the same antennas
                if(vector["x"] == 0 and vector["y"] == 0):
                    continue
                
                # Antinode coord
                antinodex, antinodey = (ant1[1]-vector["x"], ant1[2]-vector["y"])

                # Check if point in map
                if(Point_Exists(antinodex, antinodey) and [antinodex, antinodey] not in antinodes):

                    last_x = antinodex
                    last_y = antinodey
                    while(True):
                        new_x = last_x - vector["x"]
                        new_y = last_y - vector["y"]

                        if(Point_Exists(new_x, new_y)):
                            antinodes.append([new_x, new_y])
                            map[new_y][new_x] = "#"
                        else:
                            print("off", new_x, new_y)
                            break

                        last_x = new_x
                        last_y = new_y
            
            # DEBUG
    print(str(np.array(map)).replace('\'','').replace('[','').replace(']','').replace(' ',''))

    #return len(antinodes)

    result = 0
    for line in map:
        result += line.count("#")
    return result


data = Create_Data(day = 8, test = False)
frequencies, antennas = Process_Data(data)
map = [[char for char in line] for line in data] # DEBUG

print("Part One:", Part_One(frequencies, antennas))

print("Part Two:", Part_Two(frequencies, antennas))
