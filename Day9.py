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

## Solutions

# == Part One
def Part_One(data):
    pass

# == Part Two
def Part_Two(data):
    pass


data = Create_Data(day = 9, test = True)

print("Part One:", Part_One(data))

print("Part Two:", Part_Two(data))
