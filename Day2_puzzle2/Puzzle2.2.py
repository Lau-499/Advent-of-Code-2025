def div(n): #function to get divisors of a number
    list = []
    for i in range(1, n + 1):
        if n % i == 0:
           list.append(i) 
    return list

def split_in_chunks(s, chunk_size):
    list = []
    for i in range(0, len(s), chunk_size): #step through string in increments of chunk_size
        list.append(s[i:i + chunk_size]) #append substring of length chunk_size
    return list

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
        divisors = div(num_digits)
        for d in divisors:
            chunks = split_in_chunks(str(j), d) #split number into chunks of size d
            if (len(chunks) >= 2): #only consider if more than 2 chunks
                c1 = chunks[0]
                same = True
                k = 1
                while (same and k<len(chunks)):
                    if (chunks[k] != c1):
                        same = False
                    k += 1
                
                if same == True:
                    print("Invalid ID found:", j)
                    count += j
                    print("Current sum of invalid IDs:", count)  
                    break
        j += 1

print("Final sum of invalid IDs:", count)

f.close()