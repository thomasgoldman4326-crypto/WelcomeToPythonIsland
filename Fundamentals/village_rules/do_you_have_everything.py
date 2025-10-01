HasFishingRod = bool(input("Do you have your fishing rod (True/False) ? "))
Bells = int(input("How many bells do you have ? "))
if HasFishingRod == True and Bells >= 5:
	print("You can fish !")
else:
	if HasFishingRod == True:
		print("You don't have enough bells to pay the boat !")
	else:
		print("You forgot your fishing rod !")