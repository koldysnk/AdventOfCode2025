data = open("Day05/day05input.txt","r").readlines()

fresh = []

count = 0
prep = True
for line in data:
    line = line.strip()
    if line == '':
        prep = False
        continue
    if prep:
        parts = line.split('-')
        fresh.append((int(parts[0]),int(parts[1])))
    else:
        id = int(line)
        for freshers in fresh:
            if id >= freshers[0] and id <= freshers[1]:
                count += 1
                break

print(count)
