def checkValidPass(password):
	i = password[0]-1
	j = password[1]-1
	charPol = password[2]
	passStr = password[3]
	
	if(passStr[i] == charPol and passStr[j] != charPol) or (passStr[j] == charPol and passStr[i] != charPol):
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

