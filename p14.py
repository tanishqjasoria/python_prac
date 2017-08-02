def compare_version(v1,v2):
	l_v1 = [int(x) for x in v1.split('.')]
	l_v2 = [int(x) for x in v2.split('.')]
	v1 = 1000*l_v1[0] + 100*l_v1[1] + l_v1[2]
	v2 = 1000*l_v2[0] + 100*l_v2[1] + l_v2[2]
	if v1>v2:
		print("v1")
	elif v1<v2:
		print("v2")
	else:
		print("Both versions are same")
v1 = input("Input v1 :")
v2 = input("Input v2 :")
compare_version(v1,v2)
