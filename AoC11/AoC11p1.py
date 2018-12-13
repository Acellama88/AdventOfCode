import math
serial = 9810

grid = 300
i = 0
Matrix = [[0 for y in range(grid)] for x in range(grid)]

x = 0
while x < grid:
    y = 0
    while y < grid:
        rackID = x + 10
        powerLevel = (rackID * y)
        powerLevel += serial
        powerLevel = powerLevel * rackID
        powerLevel = math.floor(powerLevel / 100)
        powerLevel = (powerLevel%10)
        powerLevel -= 5
        Matrix[x][y] = powerLevel
        y += 1
    x += 1
maxX = 0
maxY = 0
maxGrid = 0
max = -1000
gridsize = 3
while gridsize < grid:
    x = 0
    while x+gridsize < grid:
        y = 0
        while y+gridsize < grid:
            power = 0
            i = 0
            while i < gridsize:
                j = 0
                while j < gridsize:
                    power += Matrix[x+i][y+j]
                    j += 1
                i += 1
            if power > max:
                max = power
                maxX = x
                maxY = y
                maxGrid = gridsize
                print(str(max), str(x), str(y), str(maxGrid), sep="-")
            y += 1
        x += 1
    gridsize += 1
    if(gridsize%10) == 0:
        print (str(gridsize))
print(str(max), str(maxX), str(maxY), str(gridsize+1), sep="-")
#x = 0
#while x < 7:
#    y = 0
#    while y < 7:
#        print(str(Matrix[x][y]),end=" ")
#        y+=1
#    print("")
#    x+=1
