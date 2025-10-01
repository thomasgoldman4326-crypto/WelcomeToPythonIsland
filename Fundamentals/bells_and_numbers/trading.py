var = int(input("Give the value of initial bells: "))
if var <5:
	print("You have to trade with at least 5 bells.")
else:
	b = 2 * var
	c = int(1.12 * b)
	d = c - var -5
	e = d //50
	f = d%50
	g = d - var
	if g < 0:
		h = "loss"
	else:
		h = "gain"
	print(f"You now have {e} bags of 50 bells and there are {f} bells in the last bag which is a total of {d} bells and a {h} of {abs(g)} bells.")