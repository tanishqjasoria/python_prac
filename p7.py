def mat_diagonal(mat,n,m):
	l=[]
	for i in range(m+n-1):
		l.append([])
	for i in range(m):
		for j in range(n):
			l[i+j].append(mat[j][i])
	return l

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
for i in range(n):
    for j in matrix[i]:
        print(j,end=' ')
    print(" ")
print("Diagonal printing of the above matrix is:")
for i in range(n+m-1):
    for j in mat_diagonal(matrix,n,m)[i]:
        print(j,end=' ')
    print(" ")
