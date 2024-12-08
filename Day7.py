import math
import numpy as np
import re

## Fetch data
def Create_Data():
    file = "Day7.txt"
    data = []

    with open(file, 'r') as f:
        for line in f:
            
            key = int(line.split(':')[0])
            value = list(map(int, line.split(':')[1].strip().split(' ')))

            data.append([key, value])
    
    return data


## Solutions
unsolved = []
def Part_One(data):
    global unsolved

    answer = 0
    for i in range(len(data)):
        expected_result = data[i][0]
        numbers = data[i][1]

        result = 0

        # Operator combinations
        combinations = []
        combination_num = len(numbers)-1

        for i in range(2 **(combination_num)):

            operators = "0"*combination_num
            shift = str(bin(i))[2:]

            operators = operators[:len(operators)-len(shift)] + shift

            operators = operators.replace("0", '+')
            operators = operators.replace("1", '*')

            #print(operators)
            combinations.append(operators)
        
        # equations
        equations = []
        for id in range(len(combinations)):
            
            eq = ""
            for i in range(len(combinations[id])):
                oper = str(combinations[id][i])
                num = str(numbers[i])

                eq = eq + num + ")" + oper

            eq = ("(" * len(combinations[id])) + eq + str(numbers[-1])
            
            equations.append(eq)

        solvable = False

        for equation in equations:
            result = eval(equation)

            if(expected_result == result):
                solvable = True                
                answer += (result)
                break
        
        if not solvable:
            unsolved.append(data[i])

        
    return answer

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))


def Part_Two(data):
    global unsolved

    answer = 0
    for i in range(len(data)):
        print(len(data), "/" ,i, end="\r")
        expected_result = data[i][0]
        numbers = data[i][1]

        result = 0

        # Operator combinations
        combinations = []
        combination_num = len(numbers)-1

        for i in range(3 **(combination_num)):

            operators = "0"*combination_num
            shift = str(ternary(i))

            operators = operators[:len(operators)-len(shift)] + shift

            operators = operators.replace("0", '+')
            operators = operators.replace("1", '*')
            operators = operators.replace("2", '|')

            #print(operators)
            combinations.append(operators)

        # equations
        equations = []
        for id in range(len(combinations)):
            
            eq = ""
            for i in range(len(combinations[id])):
                oper = str(combinations[id][i])
                num = str(numbers[i])

                eq = eq + num + ")" + oper

            eq = ("(" * len(combinations[id])) + eq + str(numbers[-1])
            
            equations.append(eq)

        solvable = False

        for equation in equations:
            
            #count_of_conc = equation.count(")|")
            #equation = equation.replace(")|","")
            #equation = equation[count_of_conc:]
            regex = r"(\([^()]*\)|[^\s()]+)"
            matches = re.finditer(regex, equation)

            last = 0

            #print(equation)
            for match in matches:
                if last==0:
                    computing = match.group()
                else:
                    computing = str(last) + match.group()
                computing = computing.replace("|", "")
                computing = computing.replace("(", "")
                computing = computing.replace(")", "")
                last = eval(computing)

                #print("     ",computing, eval(computing))

            result = last
            
            if(expected_result == result):
                solvable = True
                answer += (result)
                break
        
    return answer



data_set = Create_Data()

Part_One_result = Part_One(data_set)
print("Part One:", Part_One_result)

print("Part Two:", Part_Two(data_set))
