f = open(r"Day1_puzzle1\rotations.txt")

num = 50
cont = 0
print(num)
it = 0

for line in f:
    line = line.strip()
    letter = line[0]
    value = int(line[1:])
    if (letter == "L"):
        num -= value
    elif (letter == "R"):
        num += value
    else:
        print("Not a valid line")
    
    num = num%100
    
    it += 1

    print("Iteration ", it," : ", num)
    if (num == 0):
        cont += 1
        print("Count: ", cont)
print("Final count:", cont)
print("Thus, the password is: ", cont, ", and we reached ", num, " in the dial.", sep="")

f.close()





