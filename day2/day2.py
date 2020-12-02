def checkValidPass(password):
	minPol = password[0]
	maxPol = password[1]
	charPol = password[2]
	inputChars = list(password[3])
	count = 0
	for c in inputChars:
		if c == charPol:
			count += 1

	if count >= minPol and count <= maxPol:
		return True
	else:
		return False

def checkPasswords(passwords):
	count = 0
	for password in passwords:
		if checkValidPass(password) == True:
			count += 1
		else:
			pass
	return count

f = open("day2.in", "r")
f1 = f.readlines()
passwords = []
for line in f1:
	password = []
	data = line.split()
	nums = data[0].split('-')
	password.append(int(nums[0]))
	password.append(int(nums[1]))
	password.append(data[1][0])
	password.append(data[2])
	passwords.append(password)

print(checkPasswords(passwords))

