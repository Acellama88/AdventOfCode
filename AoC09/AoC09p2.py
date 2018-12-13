class node:
    def __init__ (self, value, prev, nxt):
        self.nxt = nxt
        self.prev = prev
        self.value = value

players = 411
marbles = 7205900
scores = {}

zero = node(0,0,0)
one = node (1,0,0)
two = node (2,0,0)
zero.prev = one
zero.nxt = two
one.prev = two
one.nxt = zero
two.prev = zero
two.nxt = one
current = two
num = 3
player = 3
while num <= marbles:
    if num%23 != 0:
        once = current.nxt
        twice= current.nxt.nxt
        new = node(num, once, twice)
        once.nxt = new
        twice.prev = new
        current = new
    else:
        if str(player) in scores:
            scores[str(player)] += num
        else:
            scores[str(player)] = num
        i = 0
        while i < 6:
            current = current.prev
            #print(str(current.value))
            i += 1
        remove = current.prev
        previous = remove.prev
        current.prev = previous
        previous.nxt = current
        scores[str(player)] += remove.value
        #print(str(remove.value) + " + " + str(num) + " = " + str(remove.value + num) + " => " +  str(player))
        #print(scores)
        
    #print(str(current.prev.value) + " " + str(current.value) + " " + str(current.nxt.value))
    #print(str(num) + " : " + str(player))
    num += 1
    player = (player % players) + 1
max = 0
maxplayer = 0
x = 0
while x < players:
    if str(x) in scores:
        if scores[str(x)] > max:
            max = scores[str(x)]
            maxplayer = x
    x += 1
print(str(maxplayer) + " : " + str(max))
#loc = current.nxt
#print(current.value)
#while loc != current:
#    print(loc.value)
#    loc = loc.nxt
