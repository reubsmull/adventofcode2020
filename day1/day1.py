
f = open("day1.in", "r")
f1 = f.readlines()
f1.sort()

x = 0
y = len(f1) - 1

while x < y:
	z = int(f1[x]) + int(f1[y])
	print(z)
	if z < 2020:
		x = x + 1
	elif z > 2020:
		y = y - 1
	else:
		print(int(f1[x]) * int(f1[y]))
		exit(1)

	
