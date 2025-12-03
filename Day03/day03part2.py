data = [[int(x) for x in line.strip()] for line in open("Day03/day03input.txt","r").readlines()]

total = 0
for row in data:
    jolt = 0
    for i in range(12):
        sub_row = row[:-(11-i)] if i<11 else row
        spark = max(sub_row)
        jolt = jolt*10 + spark
        row = row[row.index(spark)+1:]
    print(jolt)
    total += jolt
print(total)

