data = [tuple([int(x) for x in line.strip().split(",")]) for line in open("Day09/day09input.txt",'r')]
#print(data)


vmax = 0

for i, x in enumerate(data[:-1]):
    for y in data[i+1:]:
        volume = abs((max(x[0],y[0])+1-min(x[0],y[0]))*(max(x[1],y[1])+1-min(x[1],y[1])))
        vmax = max(vmax,volume)
print(vmax)
