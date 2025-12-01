def getRotation(line):
    direction = -1 if line[0]=='L' else 1
    return direction*int(line[1:])

data = [getRotation(line) for line in open("Day01/day01input.txt","r").readlines()]
print(data)

point = 50
count = 0
for direction in data:
    point = (point+direction)%100
    if point == 0:
        count+=1
    print(point)
print()
print(count)