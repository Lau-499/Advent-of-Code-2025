f = open(r"Day5_puzzle1\ingredients.txt")

lines = f.readlines()
ranges = []
ingredients = []

for line in lines:
    if (line.find("-") != -1):
        a, b = line.split("-")
        tupla = (int(a),int(b))
        ranges.append(tupla)
    else:
        if line != "\n":
            s = line.strip("\n")
            n = int(s)
            ingredients.append(n)

freshList = []

for k in ingredients:
    fresh = False
    i = 0
    while (i<len(ranges)) and (fresh == False):
        ran = ranges[i]
        if (ran[0]<= k <= ran[1]):
            fresh = True
            print("Fresh ingredient found!")
        
        i+=1
    
    if (fresh == True):
        freshList.append(k)

print("Fresh ingredients: ", len(freshList))








# print("RANGES:", ranges)
# print("INGREDIENTS", ingredients)