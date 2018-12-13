import sys

def process(loc):
    total = 0
    children = list()
    child = int(lines[loc])
    meta = int(lines[loc + 1])
    metaCount = 0
    loc += 2
    if child == 0:
        while meta > 0:
            total += int(lines[loc])
            loc += 1
            meta -= 1
        return loc, total
    else:
        while child > 0:
            result = process(loc)
            loc = result[0]
            children.append(result[1])
            child -= 1
        while metaCount < meta:
            curMeta = int(lines[loc + metaCount])
            if curMeta <= len(children) and curMeta > 0:
                total += children[curMeta-1]
                metaCount += 1
            else:
                metaCount += 1
        loc += metaCount
        return loc, total

with open('./license.txt') as f:
        lines = f.read().split(" ")
sys.setrecursionlimit(4000)
loc = 0
total = process(loc)
print(int(total[1]))
