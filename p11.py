def mult(a):
	prod = 1
	for i in a:
		prod = prod*i
	return prod
def set_mult(b):
	a=[]
	for elem in b:
		a.append(elem)
	a.sort()
	neg = [x for x in a if x<0]
	n = len(neg)
	if n%2==0 and n>0:
		if a[n]!=0:
			maxi = mult(a)
			mini = mult(a[:n-1]+a[n:])
		else:
			maxi = mult(a[:n] + a[n+1:])
			mini = mult(a[:n-1]+a[n:])
	elif n>0:
		if a[n]!=0:
			maxi = mult(a[:n-1]+a[n:])
			mini = mult(a)
		else:
			mini = mult(a[:n] + a[n+1:])
			maxi = mult(a[:n-1]+a[n+1:])
	else:
		if a[0]!=0:
			maxi = mult(a)
			mini = a[0]
		else:
			mini = 0
			maxi = mult(a[1:])
	print("Maximum product = " + str(maxi) +",       Minimum product = "+ str(mini))
arr=[]
n = int(input("Length of arr="))
for i in range(n):
    arr.append(int(input("Enter " + str(i+1) +"th element of arr : ")))
set_mult(arr)


