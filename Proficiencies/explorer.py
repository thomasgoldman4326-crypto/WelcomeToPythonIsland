name = input("Welcome fellas! What's your name? ")
bells = int(input("How many bells do you have? "))
print("Where do you want to go?\n1 - Mysterious island\n2 - Mountain\n3 - River")
found = ""
place = int(input(f"Your choice: "))
if place == 1:
	print("You chose the Mysterious Island")
	if bells >= 100:
		print("You found a treasure, but you paid 100 bells for the boat.")
		bells += 400
		found = "treasure"
	else:
		"The boat is expensive... looks like you're broke, try to find some bells on the island..."
elif place == 2:
	print("You chose the Mountain")
	print("You found a rare mineral!")
	found = "rare mineral"
	path = input("Do you want to take a dangerous shortcut? (yes/no) ")
	if path =="yes":
		print("You're brave!")
		if bells >= 200:
			bells += 100
			print("You got hurt, but you managed to buy a bandage.")
		else:
			print("You got hurt and lost your mineral...")
			found = ""
	if path == "no":
		bells += 300
		print("You took the safe path.")
elif place == 3:
	print("You chose the River")
	chose = input("Do you want to fish or swim? (fish/swim) ")
	if chose == "fish":
		print("You patiently wait for a bite.")
		bells += 150
		found = "fish"
	if chose == "swim":
		print("Maybe lady luck will smile on you.")
		bells += 50
		print("You went swimming and found 50 bells in the water.")
else:
	print("You got lost...")
if found == "":
	found = "nothing"
print("---------------------------")
print(f"{name} found: {found}")
print(f"Final bells: {bells}")
