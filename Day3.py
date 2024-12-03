import re

regex = r"mul\([0-9]{1,3},[0-9]{1,3}\)"


with open("Day3.txt",'r') as f:
    raw_lines = [line.strip() for line in f]

raw = ''.join(raw_lines)

sum = 0
matches = re.finditer(regex, raw)

for match in matches:
    code = match.group().replace('mul(', '').replace(')','')
    nums = list(map(int, code.split(',')))
    sum += nums[0] * nums[1]



raw2_splitted = re.split('(do\(\))|(don\'t\(\))', raw)

raw2 = ''
do = True
for segment in raw2_splitted:
    if(segment == None):
        continue
    elif(segment == 'do()'):
        do = True
        continue
    elif(segment == 'don\'t()'):
        do = False
        continue
    elif(do):
        raw2 = raw2 + segment
    elif(not do):
        continue


sum2 = 0
matches2 = re.finditer(regex, raw2)

for match in matches2:
    code = match.group().replace('mul(', '').replace(')','')
    nums = list(map(int, code.split(',')))
    sum2 += nums[0] * nums[1]



print("Part One:", sum)
print("Part Two:", sum2)