def isinvalid(num):
    strnum = str(num)
    for i in range(2,len(strnum)+1):
        if len(strnum)%i==0:
            half = len(strnum)//i
            parts = set([strnum[half*j:half*j+half] for j in range(0,i)])
            if len(parts)==1:
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
            #print(i)
print(total)
print(count)