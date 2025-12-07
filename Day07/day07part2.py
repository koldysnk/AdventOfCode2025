data = [list(line.strip()) for line in open("Day07/day07input.txt",'r').readlines()]
data2 = [[column for column in row] for row in data]
def display(data):
    for row in data:
        print(row)
    print()
#display(data)
#display(data2)

initial = data[0].index('S')

reference = {}
def traceParticle(y,x):
    if (y,x) in reference:
        return reference.get((y,x))
    if y == len(data)-1:
        reference[(y,x)] = 1
        return 1
    if data[y][x] == '^':
        left, right = 0,0
        if x>1:
            data2[y+1][x-1] = '|'
            left = traceParticle(y+1,x-1) 
            data2[y+1][x-1] = data[y+1][x-1]
        if x+1<len(data[y]):
            data2[y+1][x+1] = '|'
            right = traceParticle(y+1,x+1) 
            data2[y+1][x+1] = data[y+1][x+1]

        reference[(y,x)] = left+right
        return left+right
    
    center = traceParticle(y+1,x)
    reference[(y,x)] = center
    return center

print(traceParticle(0,initial)+1)
