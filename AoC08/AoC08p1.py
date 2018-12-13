import sys

total = 0

def process(loc):
    global total
    child = int(lines[loc])
    meta = int(lines[loc + 1])
    loc += 2
    while child > 0:
        loc = process(loc)
        child -= 1
    while meta > 0:
        total += int(lines[loc])
        loc += 1
        meta -= 1
    return loc

with open('./license.txt') as f:
        lines = f.read().split(" ")
sys.setrecursionlimit(4000)
loc = 0
while loc < len(lines):
    loc = process(loc)
print(int(total))
