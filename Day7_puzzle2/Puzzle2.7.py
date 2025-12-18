f = open(r"Day7_puzzle1\beams.txt")


lines = f.readlines()

cont = 0
start = None
for i in range(len(lines)):
    lines[i] = lines[i].rstrip("\n")
    line = lines[i]
    for j in range(len(line)):
        pos = lines[i][j]
        if pos == "S":
            start = (i+1,j)
            break
    if start is not None:
        break


memo = {}

def all_paths_from(r,c):
    if r<0 or r>= len(lines) or c < 0 or c>=len(lines[0]):
        return 1
    
    if (r,c) in memo:
        return memo[(r,c)]
    
    pos = lines[r][c]

    if pos == "." or pos == "S":
        ans = all_paths_from(r+1,c)
    elif pos == "^":
        ans = all_paths_from(r,c-1) + all_paths_from(r,c+1)
    else:
        ans = 1
    
    memo[(r,c)] = ans
    return ans

answer = 0
if start is not None and 0 <= start[0] < len(lines):
    sol = all_paths_from(start[0], start[1])

print("Number of times the beam splits: ", sol)
f.close()
