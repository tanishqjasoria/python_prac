def nonrepeat(ch):
	count =0
	c =''
	i=0
	while i<len(ch):
		j=i
		count =0
		while j<len(ch):
			if ch[i].lower()==ch[j].lower():
				count = count + 1
				j=j+1
			else:
				break;
			
		if count == 1:
			c = ch[i]
			break;
		i = i+count
	return c