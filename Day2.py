
def check(line):
    asc = all(line[i] < line[i+1] for i in range(len(line)-1))
    desc = all(line[i] > line[i+1] for i in range(len(line)-1))
    
    bd = max(abs(line[i] - line[i+1]) for i in range(len(line)-1))
    tbs = True if bd > 3 else False

    return True if ((asc or desc) and not tbs) else False

with open("Day2.txt", 'r') as f:
    safe = 0
    unsafe = []

    for line in f:
        line = list(map(int, line.strip().split()))
        check_result = check(line)

        safe += 1 if check_result else 0
        if(not check_result):
            unsafe.append(line)
    
    print("Part One:",safe)

    for buffer in unsafe:
        for i in range(len(buffer)):
            line = buffer.copy()

            line.pop(i)

            if(check(line)):
                safe += 1
                break
    
    print("Part Two:",safe)

        


