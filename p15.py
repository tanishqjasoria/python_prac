def rev_substr(a):
	for i in range(len(a)):
		j=i
		while j<len(a):
			if a.find(a[i:j+1][::-1])==-1:
				return False
			j=j+1
	return True
a = input("Input string str: ")
print("Output = "+str(rev_substr(a)))

