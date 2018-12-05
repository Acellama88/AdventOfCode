with open('./boxid.txt') as f:
	lines = f.read().splitlines()
twiced = 0
thriced = 0

check = 0
compare = 0
done = 0
while check < len(lines) and done == 0:
    strCheck = lines[check]
    compare = check + 1
    while compare < len(lines) and done == 0:
        loc = 0
        diff = 0
        strCompare = lines[compare]
        while loc < len(strCheck) and loc < len(strCompare) and diff < 2:
            if strCheck[loc] != strCompare[loc]:
                diff += 1
            loc += 1
        if diff < 2:
            print(strCheck)
            print(strCompare)
            done = 1
        compare += 1
    check += 1
print("End")
        
