house_price = int(input("How much for this house ? "))
bells = int(input("How many bells do you have ? "))
if house_price <= bells:
	print("You have enough bells to buy this house !")
else:
	if house_price/2 <= bells:
		print("You don't have enough money to buy the house cash but Tom Nook offers you a loan !")
	else:
		print("You don't have enough bells to buy this house, you have to save more bells.")