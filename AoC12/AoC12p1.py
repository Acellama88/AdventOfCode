class node:
    newstate = 0
    def __init__(self, state, left, right):
        self.state = state
        self.left = left
        self.right = right

class state:
    value = 0
    def __init__(self, a, b, c, d, e, result):
        if a > 0:
            self.value += 16
        if b > 0:
            self.value += 8
        if c > 0:
            self.value += 4
        if d > 0:
            self.value += 2
        if e > 0:
            self.value += 1
        self.result = result
    def compare(self, state):
        if state == self.value:
            return 1
        else:
            return 0

def count(node, stop):
    current = node
    total = 0
    count = 0 - buffer + 2
    while current.right != stop:
        if current.state > 0:
            total += count
        count += 1
        current = current.right
    return total

def printout(node,stop):
    current = node
    while current.right != stop:
        print(str(current.state),end="")
        current = current.right
    print("")

def update(node,stop):
    current = node
    while current.right != stop:
        current.state = current.newstate
        current = current.right

with open('./nodes.txt') as f:
	lines = f.read().splitlines()
initial = "#...#####.#..##...##...#.##.#.##.###..##.##.#.#..#...###..####.#.....#..##..#.##......#####..####..."
i = 0
buffer = 50
years = 100
start = node(0,0,0)
stop = node(0,0,0)
current = start
while i < buffer-1:
    new = node(0,current, stop)
    current.right = new
    current = new
    i += 1
i = 0
while i < len(initial):
    prime = 0
    if initial[i] == "#":
        prime = 1
    new = node(prime,current, stop)
    current.right = new
    current = new
    i += 1
i = 0
while i < buffer:
    new = node(0,current, stop)
    current.right = new
    current = new
    i += 1
combos = list()
i = 2
while i < len(lines):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    result = 0
    tokens = lines[i].split()
    if tokens[2] == "#":
        result = 1
    else:
        result = 0
    if tokens[0][0] == "#":
        a = 1
    else:
        a = 0
    if tokens[0][1] == "#":
        b = 1
    else:
        b = 0
    if tokens[0][2] == "#":
        c = 1
    else:
        c = 0
    if tokens[0][3] == "#":
        d = 1
    else:
        d = 0
    if tokens[0][4] == "#":
        e = 1
    else:
        e = 0
    newState = state(a, b, c, d, e, result)
    combos.append(newState)
    i += 1
start = start.right.right
current = start
year = 0
while year < years:
    current = start
    while current.right.right != stop:
        val = 0
        val = (current.left.left.state << 4) | (current.left.state << 3) | (current.state << 2) | (current.right.state << 1) | (current.right.right.state)
        #if year == 0:
            #print(str(val),end=" ")
        for x in combos:
            if x.compare(val) > 0:
                current.newstate = x.result
                break
            else:
                next
        current = current.right
        current.left.left.left.state = current.left.left.left.newstate
    current.left.left.state = current.left.left.newstate
    current.left.state = current.left.newstate
    current.state = current.newstate
    year += 1
    print(str(count(start,stop)),str(year),sep="-")
    printout(start,stop)
    #update(start,stop)
printout(start,stop)
total = count(start,stop)
print(str(total))
