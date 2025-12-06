import numpy as np

def mul(x,y):
    return x*y
def add(x,y):
    return x+y

functions = {
    '*': mul,
    '+':add
}

data = [[x for x in line.replace('\n','')] for line in open("Day06/day06input.txt",'r').readlines()]

#print(data)

total = 0
current = 0
equation = None
for i, eq in enumerate(data[-1]):
    if eq != ' ':
        equation = functions[eq]
        total += current
        print(current)
        current = 0 if eq=='+' else 1
    number = 0
    for x in range(len(data)-1):
        if data[x][i].isdigit():
            number = number*10 + int(data[x][i])
    if number >0:
        current = equation(current,number)

print(current)
print(total+current)