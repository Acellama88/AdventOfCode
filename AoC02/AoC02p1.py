with open('./boxid.txt') as f:
	lines = f.read().splitlines()
twiced = 0
thriced = 0
letters = list()
for str in lines:
    letters.clear()
    count2 = 0
    count3 = 0
    for x in str:
        if x not in letters:
            letters.append(x)
            val = str.count(x)
            if val == 2:
                count2 += 1
            if val == 3:
                count3 += 1
    if count2 > 0:
        twiced += 1
    if count3 > 0:
        thriced += 1
print(twiced * thriced)
        
