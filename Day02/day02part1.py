def isinvalid(num):
    strnum = str(num)
    if len(strnum)%2==0:
        half = len(strnum)//2
        if strnum[:half]==strnum[half:]:
            return True
    return False

data = [[int(num) for num in line.split('-')] for line in open("Day02/day02input.txt","r").readlines()[0].split(',')]

total = 0
count = 0
for line in data:
    for i in range(line[0],line[1]+1):
        if isinvalid(i):
            count+=1
            total+=i
print(total)
print(count)