f = open(r"Day5_puzzle1\ingredients.txt")

lines = f.readlines()
ranges = []

for line in lines:
    if (line.find("-") != -1):
        a, b = line.split("-")
        tupla = (int(a),int(b))
        ranges.append(tupla)

fresh = []
for ran in ranges:
    new_lo, new_hi = ran
    merged = False

    i = 0
    while i < len(fresh):
        lo, hi = fresh[i]

        if new_hi < lo - 1 or new_lo > hi + 1:
            i += 1
            continue

        new_lo = min(new_lo, lo)
        new_hi = max(new_hi, hi)
        fresh.pop(i)
        merged = True
        

    fresh.append((new_lo, new_hi))

cont = 0
for r in fresh:
    sum = r[1] - r[0] +1
    cont +=sum


print("Number of IDs considered fresh: ", cont)

f.close()