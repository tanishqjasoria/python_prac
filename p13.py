def rm_common(arra,arrb):
	unique=[]
	for i in range(len(arra)):
		if arra[:i+1].count(arra[i]) > arrb.count(arra[i]):
			unique.append(arra[i])
	for i in range(len(arrb)):
		if arrb[:i+1].count(arrb[i]) > arra.count(arrb[i]):
			unique.append(arrb[i])
	return len(unique)
arra = input("Input str1 : ")
arrb = input("Input str2 : ")
print("Output = "+str(rm_common(arra,arrb)))
