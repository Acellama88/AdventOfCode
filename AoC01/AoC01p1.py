with open('./numbers.txt') as f:
	lines = f.read().splitlines()
i = 0
for num in lines:
     i += int(num)   
print(i)
