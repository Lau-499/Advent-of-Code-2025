f = open(r"Day3_puzzle1\batteries.txt")

lines = f.readlines()

sum = 0
for line in lines:
    listaS = list(line.strip("\n"))
    nums = []
    for i in range(len(listaS)):
        nums.append(int(listaS[i]))
    
    print("Battery joltages:", nums)
    result = []
    k = 12
    i = 0
    n = len(nums)

    while len(result) < k:
        needed = k - len(result) # Still unselected numbers
        remaining = n - i # Numbers left to consider
        if remaining == needed:
            result.extend(nums[i:]) # Must take all remaining numbers
            break

        end = n - needed
        best_digit = 0
        best_pos = 0

        for pos in range(i, end + 1):
            if nums[pos] > best_digit:
                best_digit = nums[pos]
                best_pos = pos
        result.append(best_digit)
        i = best_pos + 1
    

    
    joltage = 0
    for d in result:
        joltage = joltage * 10 + d  
    print("Largest joltage in this bank: ", joltage)
    sum += joltage
    print("Current total sum of largest joltage in all banks:", sum)


f.close()
