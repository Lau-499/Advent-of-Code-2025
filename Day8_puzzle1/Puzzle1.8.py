from cmath import sqrt


f = open(r"Day8_puzzle1\box.txt")



lines = f.readlines()
boxes = []

for line in lines:
    line = line.rstrip("\n")
    x,y,z = line.split(",")
    pos = (int(x), int(y),int(z))
    boxes.append(pos)

c1 = []
c2 = []
c3 = []
# distancia euclídea = sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2 )

def distance (x1,y1,z1,x2,y2,z2):
    x = (x1-x2)**2
    y = (y1-y2)**2
    z = (z1-z2)**2
    return sqrt(x+y+z)

cont = 1000
for i in range(len(boxes)):
    pos = boxes[i]
    shortest = boxes[i+1]
    dis = distance(pos[0],pos[1],pos[2], shortest[0], shortest[1],shortest[2])
    j = 0
    

















f.close()