
f = open("day1.in", "r")
f1 = f.readlines()
f1.sort()

x = 0
y = len(f1) - 1

f2 = list(map(int, f1))

for i in range(0, len(f2)-1):
	s = set()
	curr_sum = 2020 - f2[i]
	for j in range(i+1, len(f2)):
		if(curr_sum - f2[j]) in s:
			print((f2[i] * f2[j] * (curr_sum-f2[j])))
			exit(1)
		s.add(f2[j])

	
