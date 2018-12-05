with open('./polymer.txt') as f:
	lines = f.read()
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
        loc += 1
    length = len(lines)
print(len(lines))
