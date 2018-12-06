class coord:
  def __init__(self, name, x, y):
    self.name = name
    self.x = x
    self.y = y

def Distance(x, y, coord):
    newX = abs(coord.x - x)
    newY = abs(coord.y - y)
    return newX + newY

with open('./coordinates.txt') as f:
	lines = f.read().splitlines()
pos = 0
size=500
Locations = list()
while pos < len(lines):
    tokens = lines[pos].split()
    Coordinate = coord(pos,int(tokens[0].replace(",","")),int(tokens[1]))
    Locations.append(Coordinate)
    pos += 1
Grid = [[0 for x in range(size)] for y in range(size)]
Tie = coord(-1,-1,-1)
xLoc = 0
minDistance = 10000
count = 0
while xLoc < size:
    yLoc = 0
    while yLoc < size:   
        distance = 0
        for Coord in Locations:
            ret = Distance(xLoc,yLoc, Coord)
            distance += ret
            if(distance > minDistance):
              break;
        if distance < minDistance:
            count += 1
        yLoc += 1
    if xLoc%50 == 0 and xLoc != 0:
        print(str(xLoc/5) + "% Complete")
    xLoc += 1
print(str(count))

    
