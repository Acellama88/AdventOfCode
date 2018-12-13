with open('./coordinates.txt') as f:
        lines = f.read().split(" ")
xOffset = 141
yOffset = 187
xMax = 67
yMax = 15
i = 0
Matrix = [[0 for y in range(yMax)] for x in range(xMax)]
while i < len(lines):
    print(lines[i] + " " + lines[i+1])
    Matrix[int(lines[i])-xOffset][int(lines[i+1])-yOffset] = 1
    i += 2
y = 0
while y < yMax:
    x = 0
    while x < xMax:
        if Matrix[x][y] == 1:
            print("#", end="")
        else:
            print(" ", end="")
        x += 1
    print("")
    y += 1



