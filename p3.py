def check(word,item):
	for i in  word:
		if word.count(i) <= item.count(i):
			continue
		else:
			return False
	return True
def check_list(items,word):
	x = [y for y in items if check(word,y)]
	return x
