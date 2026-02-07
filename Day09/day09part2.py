from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


data = [tuple([int(x) for x in line.strip().split(",")]) for line in open("Day09/day09input.txt",'r')]
#print(data)

polygon = Polygon(data)

vmax = 0
print()
for i, x in enumerate(data[:-1]):
    for j, y in enumerate(data[i+1:]):
        if polygon.contains(Polygon([x,(x[0],y[1]),y,(y[0],x[1])])):
            volume = abs((max(x[0],y[0])+1-min(x[0],y[0]))*(max(x[1],y[1])+1-min(x[1],y[1])))
            vmax = max(vmax,volume)
        print(f"\rProgress: {i}/{len(data)} by {j}/{len(data[i+1:])}",end='')

print()
print(vmax)
