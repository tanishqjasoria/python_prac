def editdistance(s1,s2):
	p=[]
	n = len(s1)
	m = len(s2)
	count = 0
	if n==m:
		for i in range(n):
			if(s1[i]!=s2[i]):
				count = count + 1
		if(count !=1):
			return False
		else:
			return True
	elif n-m==1:
		for i in s1:
			if i not in s2:
				p.append(i)
	elif m-n==1:
		for i in s2:
			if i not in s1:
				p.append(i)
	else:
		return False
	if len(p)==1 or len(p)==0:
		return True
	else:
		return False