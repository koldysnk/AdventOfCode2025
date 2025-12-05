data = open("Day05/day05input.txt","r").readlines()

fresh = []


for i, line in enumerate(data):
    line = line.strip()
    if line == '':
        break
    parts = line.split('-')
    start = int(parts[0])
    end = int(parts[1])
    fresh.append((start,end))
fresh.sort()

count = 0
i = 0
fresher = None
while len(fresh)>0:
    fresher = fresh.pop(0)

    searching = True
    while searching:
        if len(fresh)==0:
            searching = False
            break

        if fresh[0][0]<=fresher[1]:
            end = max(fresher[1],fresh[0][1])
            fresher = (fresher[0],end)
            fresh.pop(0)
        else:
            searching = False
    count += fresher[1]+1-fresher[0]



#print(fresh)

print(count)
