class cart:
    x = 0
    y = 0
    dir = 0
    lastdir = 0
    def __init__ (self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
        lastdir=0
    def collision(self, cart):
        if self.x == cart.x and self.y == cart.y:
            return 1
        else:
            return 0
    def move(self, x, y):
        self.x = x
        self.y = y
    def set (self, cart):
        self.x = cart.x
        self.y = cart.y
        self.dir = cart.dir
    def isHere(self, x, y):
        if self.x == x and self.y == y:
            return 1
        else:
            return 0
    def print(self):
        if self.dir == 1:
            return "^"
        if self.dir == 2:
            return ">"
        if self.dir == 3:
            return "v"
        if self.dir == 4:
            return "<"
    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+","+str(self.dir)+")"
        

def isCart(character):
    if character == "^":
        return 1
    elif character == ">":
        return 2
    elif character == "v":
        return 3
    elif character == "<":
        return 4
    else:
        return 0

def move(cart):
    if cart.dir == 1:
        cart.move(cart.x, cart.y-1)
    elif cart.dir == 2:
        cart.move(cart.x+1, cart.y)
    elif cart.dir == 3:
        cart.move(cart.x, cart.y+1)
    elif cart.dir == 4:
        cart.move(cart.x-1, cart.y)
    else:
        return 0
    return cart

def turn(cart, rail):
    if rail == "|" or rail == "-":
        return cart
    elif rail == "/":
        if cart.dir == 1:
            cart.dir = 2
        elif cart.dir == 2:
            cart.dir = 1
        elif cart.dir == 3:
            cart.dir = 4
        elif cart.dir == 4:
            cart.dir = 3
    elif rail == "\\":
        if cart.dir == 1:
            cart.dir = 4
        elif cart.dir == 2:
            cart.dir = 3
        elif cart.dir == 3:
            cart.dir = 2
        elif cart.dir == 4:
            cart.dir = 1
    elif rail == "+":
        if cart.lastdir == 0:
            cart.dir -= 1
            if cart.dir == 0:
                cart.dir = 4
            cart.lastdir += 1
        elif cart.lastdir == 1:
            cart.lastdir += 1
        elif cart.lastdir == 2:
            cart.dir = cart.dir % 4 + 1
            cart.lastdir = 0
    return cart
            
            
    
        

def setRail(top, right, bottom, left):
    railTop = 0
    railRight = 0
    railBottom = 0
    railLeft = 0
    if top == "/" or top == "\\" or top == "+" or top == "|":
        railTop = 1
    if right == "/" or right == "\\" or right == "+" or right == "-":
        railRight = 1
    if bottom == "/" or bottom == "\\" or bottom == "+" or bottom == "|":
        railBottom = 1
    if left == "/" or left == "\\" or left == "+" or left == "-":
        railLeft = 1
    if railTop > 0 and railRight > 0 and railBottom > 0 and railLeft > 0:
        middle = "+"
    elif railTop > 0 and railRight > 0 and railBottom == 0 and railLeft == 0:
        middle = "\\"
    elif railTop > 0 and railRight == 0 and railBottom > 0 and railLeft == 0:
        middle = "|"
    elif railTop > 0 and railRight == 0 and railBottom == 0 and railLeft > 0:
        middle = "/"
    elif railTop == 0 and railRight > 0 and railBottom > 0 and railLeft == 0:
        middle = "/"
    elif railTop == 0 and railRight > 0 and railBottom == 0 and railLeft > 0:
        middle = "-"
    elif railTop == 0 and railRight == 0 and railBottom > 0 and railLeft > 0:
        middle = "\\"
    else:
        middle = "?"
    return middle


        
with open('./railroad.txt') as f:
	lines = f.read().splitlines()
y = 0
carts = list()
#find carts
while y < len(lines):
    x = 0
    if "<" in lines[y] or ">" in lines[y] or "^" in lines[y] or "v" in lines[y]:
        while x < len(lines[y]):
            cartDir = isCart(lines[y][x])
            if cartDir > 0:
                addCart = cart(x, y, cartDir)
                newline = lines[y][:x] + setRail(lines[y-1][x], lines[y][x+1], lines[y+1][x], lines[y][x-1]) + lines[y][x+1:]
                #print(newline)
                lines.insert(y, newline)
                del lines[y+1]
                carts.append(addCart)
            x += 1
    y += 1
#move carts
iteration = 0
stop = 0
carts.sort()
while stop == 0:
    c = 0
    while c < len(carts):
        carts[c] = move(carts[c])
        final = turn(carts[c], lines[carts[c].y][carts[c].x])
        carts[c].set(final)
        for checkCart in carts:
            if checkCart != carts[c] and checkCart.collision(carts[c]):
                stop = 1
                print(carts[c], str(iteration))
        c += 1
    iteration += 1
    carts.sort()
    y = 0
    c = 0
    '''
    while y < len(lines):
        x = 0
        while x < len(lines[y]):
            if c < len(carts) and carts[c].isHere(x, y) > 0:
                print(carts[c].print(),end="")
                c += 1
            else:
                print(lines[y][x],end="")
            x += 1
        print("")
        y += 1
        '''
