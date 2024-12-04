
with open ("Day4_test.txt", 'r') as f:
    raw = [line.strip() for line in f]
    hexval = []

    for line in raw:
        hexval.append([ord(char) for char in line])

print(hexval)

for line in hexval:
    for i in range(len("XMAS")):
        