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
done = 0
for claim in lines:
    if(done > 0):
        break;
    tokens = claim.split()
    claim = tokens[0]
    x = int(tokens[2].split(",")[0])
    y = int(tokens[2].replace(":","").split(",")[1])
    w = int(tokens[3].split("x")[0])
    h = int(tokens[3].split("x")[1])
    i = 0
    next = 0
    while i < w and next == 0:
        j = 0
        while j < h and next == 0:
            if Fabric[x+i][y+j] > 1:
                next = 1
            j += 1
        i += 1
    if next == 0:
        print(claim)
        done = 1
print("End")
