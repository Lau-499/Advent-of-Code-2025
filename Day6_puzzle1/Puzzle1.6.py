f = open(r"Day6_puzzle1\math.txt")

lines = f.readlines()

sum = 0
all = []
for line in lines:
    nums = line.split()
    if (lines.index(line) != 4):
        for n in nums:
            nums[nums.index(n)] = int(n)
    all.append(nums)

solutions = []
for i in range(len(all[0])):
    if (all[4][i] == "+"):
        s = all[0][i] + all[1][i] + all[2][i] + all[3][i]
        sum += s
        solutions.append(s)
    elif (all[4][i] == "*"):
        m = all[0][i] * all[1][i] * all[2][i] * all[3][i]
        sum += m
        solutions.append(m)

print("Solutions: ", solutions)

print("Grand total = ", sum)

f.close()