f = open(r"Day3_puzzle1\batteries.txt")

lines = f.readlines()

sum = 0
for line in lines:
    listaS = list(line.strip("\n"))
    nums = []
    for i in range(len(listaS)):
        nums.append(int(listaS[i]))
    
    print("Battery joltages:", nums)
    max1 = 0
    max2 = 0
    
    for i in nums:
        if (i > max1) and (nums.index(i) != len(nums)-1):
            
            max1 = i

    for i in range(nums.index(max1)+1, len(nums)):
        if nums[i] > max2:
            max2 = nums[i]

   
    
    print("Highest joltage:", max1)
    print("Second highest joltage:", max2)
    joltage = (max1*10) + max2
    print("Largest joltage in this bank: ", joltage)
    sum += joltage
    print("Current total sum of largest joltage in all banks:", sum)



