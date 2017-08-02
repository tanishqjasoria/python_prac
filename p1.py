def search(pat,txt):
	count = 0
	n = len(txt)
	m = len(pat)
	for i in range(n-m+1):
		if txt[i:i+m] == pat:
			count = count+1
	return count