def min_area(lst):
	x=[]
	y=[]
	for i in lst:
		x.append(int(i[1]))
		y.append(int(i[3]))
	area = (abs(max(y)-min(y)))*(abs(max(x)-min(x)))
	return area



def min_area_1(lst):
	for i in range(len(lst)):
		j =i
		area1 = -1
		while j<len(lst):
			minarea = min_area(lst[i:j+1])
			if area1==-1 or minarea<area1:
				area1 = minarea
			j = j + 1
	return area1
lst =[]
n = int(input("Enter no of cordinates: "))
for i in range(n):
    lst.append("("+str(input(str(i+1) + "th x coordinate: ")) + ","+str(input(str(i+1) + "th y coordinate: ")))
print("Area of smallest rectangle including all point = " + str(min_area(lst)))
print("Area of smallest rectangle excluding atmost 1 point = " + str(min_area_1(lst)))
    

    
