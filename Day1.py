
left, right = [], []

with open("Day1.txt", 'r') as f:
    for line in f:
        line = line.split()

        left.append(int(line[0]))
        right.append(int(line[1]))


left.sort()
right.sort()

sum = 0
similarity = 0
for l,r in zip(left, right):
    sum += abs(l - r)

    similarity += (right.count(l) * l)


print("Sum:", sum)
print("Similarity:", similarity)
