f = open(r"Day7_puzzle1\beams.txt")


lines = f.readlines()

dict = {}
cont = 0
start = None
for i in range(len(lines)):
    lines[i] = lines[i].rstrip("\n")
    line = lines[i]
    for j in range(len(line)):
        pos = lines[i][j]
        if pos == "S":
            start = (i+1,j)


beams = set()

if (start != None) and (0<= start[0] <len(lines)):
    beams.add(start)

split_done = set()
while beams:
    new_beams= set()
    for (r,c) in beams:
        if not (0 <= int(r) < len(lines) and 0 <= int(c) < len(lines[0])):
            continue
    
        pos = (r,c)
        if lines[r][c] == ".":
            new_beams.add((r+1,c))
        elif lines[r][c] == "^":
            if (r,c) not in split_done:
                split_done.add((r,c))
                cont +=1
                new_beams.add((r,c-1))
                new_beams.add((r,c+1))

    beams = new_beams   


print("Number of times the beam splits: ", cont)
f.close()
