with open('./numbers.txt') as f:
	lines = f.read().splitlines()
i = 0
count = 0
Frequencies = list()
while i not in Frequencies:
	Frequencies.append(i)
	i += int(lines[count%len(lines)])
	count += 1
print(i)
