with open('./claims.txt') as f:
	lines = f.read().splitlines()
size = 1000
Fabric = [[0 for x in range(size)] for y in range(size)]
for claim in lines:
    tokens = claim.split()
    claim = tokens[0]
    x = int(tokens[2].split(",")[0])
    y = int(tokens[2].replace(":","").split(",")[1])
    w = int(tokens[3].split("x")[0])
    h = int(tokens[3].split("x")[1])
    i = 0
    while i < w:
        j = 0
        while j < h:
            Fabric[x+i][y+j] += 1
            j += 1
        i += 1
countx = 0
overlap = 0
while countx < size:
    county = 0
    while county < size:
        if(Fabric[countx][county] >= 2):
            overlap += 1
        county += 1
    countx += 1
print(overlap)
