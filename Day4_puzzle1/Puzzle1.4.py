print("EMPIEZA EL PROGRAMA")
f = open(r"Day4_puzzle1\paper.txt")

lines = f.readlines()


dict = {}
for i in range(len(lines)): #i=row
    line = lines[i].strip("\n")
    for j in range(len(line)): #j=column
        roll = line[j]
        pos = (i, j)
        title = roll+"_"+str(i)+","+str(j)
        dict[title] = pos


rolls = []

for key in dict:
    if (key.find("@") != -1) :
        rolls.append(dict[key])

accessable = []
rolls_set = set(rolls)
for (r, c) in rolls:
    count = 0
    for dr,dc in [(-1,-1), (-1,0),(-1,1),(0,-1),(0,1),(1,-1), (1,0), (1,1)]:
        rr, cc = r+dr,c+dc
        if (0<=rr<=134) and (0<=cc<=134) and ((rr,cc) in rolls_set):
            count += 1
    
    if count < 4:
        accessable.append((r,c)) 


print("Número de rollos accesibles:",str(len(accessable)))

f.close()
        

        