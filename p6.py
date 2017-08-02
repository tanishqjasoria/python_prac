def common(a,n,m):
	b = True
	l =[]
	common=[]
	for i in range(n):
		l = l + a[i]
	for i in range(len(l)):
		b = True
		for j in range(n):
			b = b and (l[i] in a[j])
		if b == True and l[i] not in common:
			common.append(l[i])
	return common


n = int(input('number of rows, n = '))
m = int(input('number of columns, m = '))
matrix = []; columns = []
for i in range(0,n):
  matrix += [0]
for j in range (0,m):
  columns += [0]
for i in range (0,n):
  matrix[i] = columns[:]
print(matrix)
for i in range (0,n):
  for j in range (0,m):
    print ('entry in row: ',i+1,' column: ',j+1)
    matrix[i][j] = int(input())
print("Input Matrix: ")
print (matrix)
for i in common(matrix,n,m):
    print(i,end=' ')

