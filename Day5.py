import math

rules = []
updates = []

wrong_updates = []

with open("Day5.txt", 'r') as f:

    change = False

    for line in f:
        line = line.strip()
        if(len(line)==0):
            change = True
            continue
    
        if not change:
            rules.append(line.split('|'))
        else:
            updates.append(line.split(','))

result = 0
for update in updates:
    error = False
    for page in range(len(update)):

        after = False
        for check in range(0, len(update)):

            if(update[page] == update[check]):
                after = True
                continue

            if(after):
                check_arr = [update[page], update[check]]
            else:
                check_arr = [update[check], update[page]]

            ## Check Rules every page with every page
            
            if( check_arr in rules):
                continue
            else:
                error = True
                break
            
        if(error):
            break

    if(error):
        pass
        wrong_updates.append(update)
    else:
        middle = len(update)//2
        result += int(update[middle])

print("Part one: ", result)


result = 0
for update in wrong_updates:

    error = False
    for page in range(len(update)):

        after = False
        check = 0
        while check < len(update):

            if(update[page] == update[check]):
                after = True
                check += 1
                continue

            if(after):
                check_arr = [update[page], update[check]]
            else:
                check_arr = [update[check], update[page]]

            ## Check Rules every page with every page
            
            if( check_arr in rules):
                check += 1
                continue
            else:
                update[page], update[check] = update[check], update[page]
                check = 0
                after = False
            
        if(error):
            break

    if(error):
        pass
    else:
        middle = len(update)//2
        result += int(update[middle])

print("Part two: ", result)