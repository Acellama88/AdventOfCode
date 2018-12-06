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
while xLoc < size:
    yLoc = 0
    while yLoc < size:
        choosenCoord = Tie
        closestCoord = 1000000
        for Coord in Locations:
            ret = Distance(xLoc,yLoc, Coord)
            if ret < closestCoord:
                choosenCoord = Coord
                closestCoord = ret
            elif ret == closestCoord:
                choosenCoord = Tie
        Grid[xLoc][yLoc] = choosenCoord.name
        yLoc += 1
    if xLoc%50 == 0 and xLoc != 0:
        print(str(xLoc/5) + "% Complete")
    xLoc += 1
print ("Distances Complete")
Counts = {}
xLoc = 0
while xLoc < size:
    yLoc = 0
    while yLoc < size:
        if str(Grid[xLoc][yLoc]) in Counts:
            Counts[str(Grid[xLoc][yLoc])] += 1
        else:
            Counts[str(Grid[xLoc][yLoc])] = 1
        yLoc += 1
    xLoc += 1
print ("Location Area Calculated")
xLoc = 0
yLoc = 0
while xLoc < size:
    if str(Grid[xLoc][yLoc]) in Counts:
        Counts.pop(str(Grid[xLoc][yLoc]))
    xLoc += 1
    
xLoc = 0
yLoc = 0
while yLoc < size:
    if str(Grid[xLoc][yLoc]) in Counts:
        Counts.pop(str(Grid[xLoc][yLoc]))
    yLoc += 1

xLoc = 0
yLoc = size-1
while xLoc < size:
    if str(Grid[xLoc][yLoc]) in Counts:
        Counts.pop(str(Grid[xLoc][yLoc]))
    xLoc += 1
    
xLoc = size-1
yLoc = 0
while yLoc < size:
    if str(Grid[xLoc][yLoc]) in Counts:
        Counts.pop(str(Grid[xLoc][yLoc]))
    yLoc += 1
print ("Removed infinite options")
most = -1
name = -1
xLoc = 0
while xLoc < size:
    if str(xLoc) in Counts:
        if Counts[str(xLoc)] > most:
            name = xLoc
            most = Counts[str(xLoc)]
    xLoc += 1
print(str(most) + " " + str(name))

    
