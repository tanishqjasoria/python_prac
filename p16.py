def substr(str0):
	unique = []
	for i in range(len(str0)):
		j=i
		while j<len(str0):
			g = str0[i:j+1]
			if g not in unique:
				unique.append(g)
			j = j + 1
	unique.sort()
	return unique
str0 = input("Input the string:")
print("Output = "+str(substr(str0)))
