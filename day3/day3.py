

def countTrees(input):
	x = 0
	flag = 0
	count = 0
	for line in input:
		if flag == 0:
			flag = 1
			continue
		x = incrementPosition(x)
		if(line[x] == '#'):
			count += 1
	return count

def incrementPosition(x):
	x += 3
	x = x % 31
	return x

f = open('day3.in', 'r')
f1 = f.readlines()
print(countTrees(f1))