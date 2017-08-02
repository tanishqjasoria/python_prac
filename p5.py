def is_iso(str1,str2):
	total = 256
	m = len(str1)
	n = len(str2)
	chk = [False] * total
	code = [-1] * total
	if m!=n:
		return False
	else:
		for i in range(n):
			if code[ord(str1[i])] == -1:
				if chk[ord(str2[i])] == True:
					return False
				chk[ord(str2[i])] = True
				code[ord(str1[i])] = str2[i]
			elif code[ord(str1[i])] != str2[i]:
				return False
		return True
str1 = str(input("Input String 1 : "))
str2 = str(input("Input String 2 : "))
print(is_iso(str1,str2))
