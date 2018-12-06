with open('./schedule.txt') as f:
	lines = f.read().splitlines()
lines.sort()
with open('./sorted.txt', 'w') as f:
    for x in lines:
        f.write(x + "\n")
