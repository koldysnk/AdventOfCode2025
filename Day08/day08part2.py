import math
data = [tuple([int(x) for x in line.strip().split(',')]) for line in open("Day08/day08input.txt",'r')]

def distance(x,y):
    a,b,c = (x[0]-y[0]),(x[1]-y[1]),(x[2]-y[2])
    return math.sqrt(a**2 + b**2 + c**2)

print(data)

distances = []

for i, x in enumerate(data[:-1]):
    for y in data[i+1:]:

        dis = distance(x,y)
        distances.append((dis,x,y))

distances.sort()

connections = []

for wire in distances:
    connection = set(wire[1:])
    dis,x,y = wire
    if x == (162,817,812) and y == (425,690,689):
        print(dis)
    
    i = 0
    while i<len(connections):
        if x in connections[i] or y in connections[i]:
            connection = connection.union(connections[i])
            connections.pop(i)
        else:
            i+=1
    connections.append(connection)
    if len(connection) == len(data):
        print(x[0]*y[0])
        break
