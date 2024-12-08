import math
import numpy as np

## Fetch data
def Create_Data(day, test=False):
    if test:
        file = f"Day{day}_test.txt"
    else:
        file = f"Day{day}.txt"

    with open(file, 'r') as f:
        raw = [line.strip() for line in f]

    return raw

## Solutions

# == Part One
def Part_One():
    pass

# == Part Two
def Part_Two():
    pass


data = Create_Data("",test=False)

print("Part One:", Part_One(data))

print("Part Two:", Part_Two(data))
