data = [[int(x) for x in line.strip()] for line in open("Day03/day03input.txt","r").readlines()]

total = 0
for row in data:
    jolt = max(row[:-1])
    jolt = 10*jolt + max(row[row.index(jolt)+1:])
    total += jolt
print(total)

