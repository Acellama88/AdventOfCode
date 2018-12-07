class step:
    prereqs = list()
    def __init__(self, name):
        self.name = name
    def isFree(self,req):
        return len(prereqs)
    def addStep(self, req):
        self.prereqs.append(req)
    def remStep(self, req):
        if req in self.prereqs:
            self.prereqs.pop(req)
        return len(prereqs)

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
for x in lines:
    tokens = x.split()
    getStep(tokens[7], line).addStep(tokens[1])
for x in line:
    print(x.prereqs[0])
for x in line:
    if x.isFree == 0:
        line.pop(x)
        queue.append(x)
while len(queue) > 0:
    queue.sort()
    answer += queue[0].name
    for x in line:
        if x.remStep(queue[0].name) == 0:
            line.pop(x)
            queue.append(x)
    del queue[0]
print("Answer is: " + answer)
