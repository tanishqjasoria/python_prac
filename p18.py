def num_char_cardinal(i1,i2):
	for i in range(len(i1)):
		for j in range(len(i2)):
			if j>i:
				print("<"+str(i1[i])+",\""+str(i2[j])+"\">",end=' ')
arra =[]
arrb =[]
n = int(input("Length of I1="))
for i in range(n):
    arra.append(int(input("Enter " + str(i+1) +"th element of I1 : ")))
n = int(input("Length of I2="))
for i in range(n):
    arrb.append(input("Enter " + str(i+1) +"th element of I2 : "))
num_char_cardinal(arra,arrb)
