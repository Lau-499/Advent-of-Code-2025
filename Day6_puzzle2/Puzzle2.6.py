f = open(r"Day6_puzzle1\math.txt")


lines = f.readlines()
all = []
for line in lines:
    all.append(line.rstrip("\n"))

# We secure the 5 rows
row0, row1, row2, row3, op_line = all[0], all[1], all[2], all[3], all[4]

# We make sure all the rows have the same length
L = max(len(row0), len(row1), len(row2), len(row3), len(op_line))
row0 = row0.ljust(L)
row1 = row1.ljust(L)
row2 = row2.ljust(L)
row3 = row3.ljust(L)
op_line = op_line.ljust(L)

# We are going to make sure the operator is the one we must use, by using the separators (columns with all spaces)
seps = []
for i in range(L):
    if row0[i] == row1[i] == row2[i] == row3[i] == op_line[i] == " ":
        seps.append(i) # Position of the separators between columns

seps.append(L) # We add the last position to be able to close the last line


# We convert the separators into segments
segments = []
start = 0
for i in seps: 
    if i > start:
        segments.append((start, i))  # [start, c)
    start = i + 1
# Now we know the index of where the operation starts and ends


# For each segment, we take the operator.
ops = []
for a, b in segments:
    seg = op_line[a:b].strip() # Here we have the operator "*" or "+"
    ops.append(seg)

# We create the correct numbers
onlyNums = []
for a, b in segments:
    # Numbers for each segment per row
    b0 = row0[a:b]
    b1 = row1[a:b]
    b2 = row2[a:b]
    b3 = row3[a:b]

    nums = []
    for j in range(b - a):
        s = b0[j] + b1[j] + b2[j] + b3[j]
        if s.strip() != "":          # if it's not a separator
            nums.append(int(s))
    onlyNums.append(nums)

total = 0
solutions = []

for nums, op in zip(onlyNums, ops): #We pair both numbers and operators position per position
    if op == "+":
        s = 0
        for x in nums:
            s += x
    elif op == "*":
        s = 1
        for x in nums:
            s *= x
    

    solutions.append(s)
    total += s

print("Grand total =", total)
