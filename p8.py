def min_swap(arra,arrb):
	count =0
	#print(arra,arrb)
	if sorted(arra)==sorted(arrb):
		#print(arra,arrb)
		#print("in if")
		for i in range(len(arra)):
			if arra[i]==arrb[i]:
				#print("in in if")
				continue
			else:
				#print("in in else")
				index = arrb.index(arra[i])
				temp = arrb[i]
				arrb[i] = arrb[index]
				arrb[index]=temp
				count = count +1
	else:
		#print("in else")
		count = -1
	return count
arra=[]
arrb=[]
n = int(input("Length of arrA="))
for i in range(n):
    arra.append(input("Enter " + str(i+1) +"th element of arrA : "))
n = int(input("Length of arrB="))
for i in range(n):
    arrb.append(input("Enter " + str(i+1) +"th element of arrB : "))
print("Output = "+str(min_swap(arra,arrb)))
