with open('./polymer.txt') as f:
	readline = f.read()
length = len(readline)
lines = readline
oldlength = 0
alphabet = "abcdefghijklmnopqrstuvwxyz"
bestlength = 1000000000
aLoc = 0
while aLoc < len(alphabet):
    lines = readline.replace(alphabet[aLoc],"").replace(alphabet[aLoc].upper(),"")
    length = len(lines)
    oldlength = 0
    while oldlength != length:
        oldlength = length
        loc = 0
        while loc < len(lines)-1:
            match = 0
            if lines[loc].islower():
                if lines[loc].upper() == lines[loc+1]:
                    match = 1
            else:
                if lines[loc].lower() == lines[loc+1]:
                    match = 1
            if match > 0:
                lines = lines[:loc] + lines[loc+2:]
            else:
                loc += 1
        length = len(lines)
    if length < bestlength:
        bestlength = length
    print(alphabet[aLoc] + " " + str(length))
    aLoc += 1
print(bestlength)
