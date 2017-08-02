def rev(arr,k):
	a = []
	i=0
	while i<len(arr):
		a = a+arr[i:i+k][::-1]
		i =i+3
	return a
arr=[]
n = int(input("Length of arr="))
for i in range(n):
    arr.append(int(input("Enter " + str(i+1) +"th element of arr : ")))
k = int(input("Value of k: "))
print("Output = "+str(rev(arr,k)))
