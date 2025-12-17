f = open(r"Day2_puzzle1\ids.txt")

all = f.read()

ranges = all.split(",")

print(ranges)

n = len(ranges)
print("Number of ranges:", n)
count = 0
for i in range(n):
    id1, id2 = ranges[i].split("-")
    id1 = int(id1)
    id2 = int(id2)
    print("Range ", i+1, ": from ", id1, " to ", id2, sep="")
    j = id1
    while (j <= id2):
        num_digits = len(str(j))
        if (num_digits%2 == 0):
            mid = num_digits//2
            first_half = int(str(j)[:mid])
            second_half = int(str(j)[mid:])
            if (first_half == second_half):
                print("Invalid ID found:", j)
                count += j
                print("Current sum of invalid IDs:", count)       
        j += 1

print("Final sum of invalid IDs:", count)
f.close()