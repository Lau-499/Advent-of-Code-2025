f = open(r"Day1_puzzle1\rotations.txt")

num = 50
cont = 0
print(num)
it = 0

for linea in f:
    line = linea.strip()
    print(line)
    letter = line[0]
    value = int(line[1:]) # number of steps we need to take, either to the left or to the right
    if (letter == "L"):
        click = -1 # step to the left, decrease the number
    elif (letter == "R"):
        click = 1 # step to the right, increase the number
    else:
        print("Not a valid line")
    
    for i in range(value): # Loop for the number of clicks
        num += click
        if (num < 0):
            num = 99
        elif (num > 99):
            num = 0
        
        zero = 0
        if (num == 0):
            cont += 1
            zero += 1
        
    print("We reached 0: ", zero, " times.\n Count: ", cont, sep="")
    
    it += 1
    print("Iteration: ", it, ", current number: ", num, sep="")

    
print("Final count:", cont)
print("Thus, the password is: ", cont, ", and we reached ", num, " in the dial.", sep="")

f.close()





