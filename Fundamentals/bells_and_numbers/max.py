var_1 = int(input("Give a value for a: "))
var_2 = int(input("Give a value for b: "))
var_3 = int(input("Give a value for c: "))
var_4 = int(input("Give a value for d: "))
if var_1 > var_2:
	if var_1 > var_3:
		if var_1 > var_4:
			print(var_1)
		else :
			print(var_4)
	else:
		if var_3 > var_4:
			print(var_3)
		else:
			print(var_4)
else:
	if var_2 > var_3:
		if var_2 > var_4:
			print(var_2)
		else:
			print(var_4)
	else:
		if var_3 > var_4:
			print(var_3)
		else:
			print(var_4)
	