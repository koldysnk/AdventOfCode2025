def getRotation(line):
    direction = -1 if line[0]=='L' else 1
    return (direction,int(line[1:]))

data = [getRotation(line) for line in open("Day01/day01input.txt","r").readlines()]
print(data)

point = 50
count = 0
for i, direction in enumerate(data):
    for i in range(direction[1]):
        point = (point+direction[0])%100
        if point == 0:
            count+=1
            print(count)
print()
print(count)