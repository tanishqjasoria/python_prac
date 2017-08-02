def small_sub(arr):
	mult = 0
	len_small = len(arr)
	arr_small = []
	for i in range(len(arr)):
		j=i
		mult = 0
		while j<len(arr):
			mult = mult + arr[j]
			#print(mult)
			if mult == len(arr) and (j-i+1)<len_small:
				#print("in if")
				arr_small = arr[i:j+1]
				len_small = len(arr_small)
				#print(arr_small)
				break
			j = j+1
		print('\n')
	return arr_small
arr=[]
n = int(input("Length of arr="))
for i in range(n):
    arr.append(int(input("Enter " + str(i+1) +"th element of arr : ")))
print("Output = "+str(small_sub(arr)))
