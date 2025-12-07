data = [list(line.strip()) for line in open("Day07/day07input.txt",'r').readlines()]
#print(data)

initial = data[0].index('S')

queue = [(0,initial)]
used = set()
count = 0
while len(queue)>0:
    current = queue.pop()
    if current in used:
        continue
    used.add(current)

    y,x = current
    if y>=len(data) or x<0 or x>=len(data[y]):
        continue

    if data[y][x] == '^':
        count +=1
        queue.append((y+1,x-1))
        queue.append((y+1,x+1))
    else:
        queue.append((y+1,x))

print(count)

