def sum_pair(arr):
	x = [abs(a-b) for a in arr for b in arr]
	y = sum(x)/2
	return y
arr=[]
n = int(input("Length of arr="))
for i in range(n):
    arr.append(int(input("Enter " + str(i+1) +"th element of arr : ")))
print("Output = "+str(sum_pair(arr)))
