print("PROGRAM START")
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

def rolls(dict):
    rolls = []
    for key in dict:
        if (key.find("@") != -1) :
            rolls.append(dict[key])
    return rolls


def accessable(dict):
    rols = rolls(dict)
    accessable = []
    rolls_set = set(rols)
    for (r, c) in rols:
        count = 0
        for dr,dc in [(-1,-1), (-1,0),(-1,1),(0,-1),(0,1),(1,-1), (1,0), (1,1)]:
            rr, cc = r+dr,c+dc
            if (0<=rr<=134) and (0<=cc<=134) and ((rr,cc) in rolls_set):
                count += 1
        if count < 4:
            accessable.append((r,c))
    return accessable

def removeRoll(d, r, a):
    for key in list(d.keys()):
        if d[key] in a: # if a coordinate is in the list of accessible rolls
            # We find out what that roll would be called if removed, and what its value would be
            coordi = d[key][0]
            coordj = d[key][1]
            s = "._"+str(coordi)+","+str(coordj)
            value = d[key]
            #We add it to the dictionary 
            d[s] = value
            #We remove the roll 
            d.pop(key)
            #We update the count of removed rolls
            r +=1
    return d, r

removed = 0
acc = accessable(dict)
print("Accessable: ", str(len(accessable(dict))))
print("Length dictionary: ", str(len(dict)))
print("Removed: ", str(removed))

while (len(acc) > 0):
    dict, removed = removeRoll(dict, removed, acc)
    acc = accessable(dict)
    print("ITERATION ENDED")
    print("Accesable: ", str(len(accessable(dict))))
    print("Removed: ", str(removed))


print("PROGRAM ENDED")
print("Accesable: ", str(len(accessable(dict))))
print("Removed: ", str(removed))


f.close()







        
