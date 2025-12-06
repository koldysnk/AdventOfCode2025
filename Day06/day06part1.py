def mul(x,y):
    return x*y
def add(x,y):
    return x+y

functions = {
    '*': mul,
    '+':add
}

data = open("Day06/day06input.txt",'r').readlines()

#print(data)

results = [int(x) for x in data[0].strip().split(' ') if x.isdigit()]
equations = [functions[x] for x in data[-1].strip().split(' ') if x!='']

for line in data[1:-1]:
    line = [int(x) for x in line.strip().split(' ') if x.isdigit()]
    for i, x in enumerate(line):
        results[i] = equations[i](results[i],x)

print(sum(results))
