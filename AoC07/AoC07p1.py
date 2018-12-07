class step:
    prereqs = list()
    def __init__(self, name):
        self.name = name
        self.prereqs = []
    def isFree(self):
        return len(self.prereqs)
    def addStep(self, req):
        self.prereqs.append(req)
    def remStep(self, req):
        i = 0
        while i < len(self.prereqs):
            if self.prereqs[i] == req:
                del self.prereqs[i]
            else:
                i += 1
        return len(self.prereqs)
    def __lt__(self, other):
        return self.name < other
    def __gt__(self, other):
        return self.name > other

def getStep(name, queue):
    for x in queue:
        if x.name == name:
            return x

with open('./steps.txt') as f:
	lines = f.read().splitlines()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = ""
line = list()
queue = list()
for x in alphabet:
    newClass = step(x)
    line.append(newClass)
    #check
for x in lines:
    tokens = x.split()
    getStep(tokens[7], line).addStep(tokens[1])
    #check
i = 0
while i < len(line):
    if line[i].isFree() == 0:
        queue.append(line[i])
        del line[i]
    else:
        i += 1
while len(queue) > 0:
    queue.sort()
    answer += queue[0].name
    i = 0
    while i < len(line):
        if line[i].remStep(queue[0].name) == 0:
            queue.append(line[i])
            del line[i]
        else:
            i += 1
    del queue[0]
print("Answer is: " + answer)
