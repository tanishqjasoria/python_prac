def num_char(i1,i2):
	for i in i1:
		for j in i2:
			print("<"+str(i)+",\""+str(j)+"\">",end=' ')
arra =[]
arrb =[]
n = int(input("Length of I1="))
for i in range(n):
    arra.append(int(input("Enter " + str(i+1) +"th element of I1 : ")))
n = int(input("Length of I2="))
for i in range(n):
    arrb.append(input("Enter " + str(i+1) +"th element of I2 : "))
num_char(arra,arrb)
