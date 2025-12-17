f = open(r"Day7_puzzle1\beams.txt")


lines = f.readlines()

dict = {}
for i in range(len(lines)): #i=row
    line = lines[i].strip("\n")
    for j in range(len(line)): #j=column
        split = line[j]
        pos = (i, j)
        title = split+"_"+str(i)+","+str(j)
        dict[title] = pos


beams = []
for k, v in dict:
    if k.find("S") != -1:
        beams.append(v[0]+1,v[1])
    elif (k.find("^") != -1) and ((v[0]-1,v[1]) in beams):
        beams.append(v[0], v[1]-1)
        beams.append(v[0], v[1]+1)

