class step:
    prereqs = list()
    time = 0
    def __init__(self, name, time):
        self.name = name
        self.time = time
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

class elf:
    time = 0
    def __init__(self):
        self.step = step("", 0)
        time = 0
    def isFree(self):
        return self.time
    def decTime(self):
        if self.time > 0:
            self.time -= 1
        return self.time
    def setStep(self, step):
        self.step = step
        self.time = step.time

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
elves = list()
count = 61
for x in alphabet:
    newClass = step(x, count)
    line.append(newClass)
    count += 1
    #check
for x in lines:
    tokens = x.split()
    getStep(tokens[7], line).addStep(tokens[1])
    #check
i = 0
while i < 5:
    elves.append(elf())
    i += 1
i = 0
while i < len(line):
    if line[i].isFree() == 0:
        queue.append(line[i])
        del line[i]
    else:
        i += 1
#edit
count = 0
elvesBusy = 0
while len(line) > 0 or len(queue) > 0 or elvesBusy > 0:
    queue.sort()
    #assign elf
    if len(queue) > 0:
        for elf in elves:
            if elf.isFree() == 0:
                elf.setStep(queue[0])
                del queue[0]
                elvesBusy += 1
                break
    if len(queue) == 0 or elvesBusy >= 5:
        #do work
        count += 1
        for elf in elves:
            if elf.isFree() != 0:
                if elf.decTime() == 0:
                    answer += elf.step.name
                    elvesBusy -= 1
                    i = 0
                    while i < len(line):
                        if line[i].remStep(elf.step.name) == 0:
                            queue.append(line[i])
                            del line[i]
                        else:
                            i += 1
print(answer)
print("Answer is: " + str(count))
