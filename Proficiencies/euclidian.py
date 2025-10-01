a = int(input("Give a value for a: "))
b = int(input("Give a value for b: "))
if b == 0:
	"Cannot Divide by 0"
if b < 0:
	r = (a%(-b))
	q = -(a//(-b))
	print(f"{a} = {b} * {q} + {r}")
else:
	r = a % b
	q = a // b
	print(f"{a} = {b} * {q} + {r}")
	