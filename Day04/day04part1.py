data = [list(line.strip()) for line in open("Day04/day04input.txt","r").readlines()]

data2 = [[x for x in row] for row in data]

count = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        subcount = 0
        if data[y][x] != '@':
            continue
        if y > 0:
            if x >0 and data[y-1][x-1] == '@':
                subcount +=1
            if data[y-1][x] == '@':
                subcount +=1
            if x <len(data[0])-1 and data[y-1][x+1] == '@':
                subcount +=1
        if y < len(data)-1:
            if x >0 and data[y+1][x-1] == '@':
                subcount +=1
            if data[y+1][x] == '@':
                subcount +=1
            if x <len(data[0])-1 and data[y+1][x+1] == '@':
                subcount +=1
        if x >0 and data[y][x-1] == '@':
            subcount +=1
        if x <len(data[0])-1 and data[y][x+1] == '@':
            subcount +=1
        if subcount<4:
            count+=1
            data2[y][x] = 'x'
print(count)
                