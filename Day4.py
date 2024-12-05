import numpy as np

with open ("Day4.txt", 'r') as f:
    raw = [line.strip() for line in f]
    matrix = []

    for line in raw:
        matrix.append([char for char in line])

    matrix = np.array(matrix)

class Error(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def exists(idx, idy):
    if ((0 <= idx < len(matrix)) and (0 <= idy < len(matrix[idx]))):
        return True
    else:
        return False



def compass(x,y, dir, buffer = []):
    buffer.append(matrix[y][x])

    if (dir == "S"):  nextx, nexty = x,   y+1
    elif (dir == "SE"): nextx, nexty = x+1, y+1
    elif (dir == "SW"): nextx, nexty = x-1, y+1
    else:
        raise Error("wrong direction")

    if(exists(nextx, nexty)):
        compass(nextx, nexty, dir, buffer)
        
    return buffer.copy()

data = []

for i in range(4):
    for x in range(len(matrix)):
        if (x==0):
            [data.append(compass(x, 0, direction, [])) for direction in ["S", "SW"]]
        else:
            [data.append(compass(x, 0, direction, [])) for direction in ["S", "SE", "SW"]]            
    
    matrix = np.rot90(matrix)


strings = [''.join(data[i]) for i in range(len(data))]
result = sum(string.count("XMAS") for string in strings)

print("Part one:", result)

result = 0
for y in range(len(matrix)-2):
    for x in range (len(matrix[y])-2):

        windowx = [x, x+1, x+2]
        windowy = [y, y+1, y+2]

        diagonal1 = ""
        diagonal2 = ""

        for idx,idy in zip(windowx, windowy):
            diagonal1 = diagonal1 + matrix[idy][idx]

        windowx.reverse()
        for idx,idy in zip(windowx, windowy):
            diagonal2 = diagonal2 + matrix[idy][idx]

        result = result + (1 if (diagonal1=="SAM" or diagonal1=="MAS") and \
                                (diagonal2=="SAM" or diagonal2=="MAS") else 0)

print("Part two:", result)