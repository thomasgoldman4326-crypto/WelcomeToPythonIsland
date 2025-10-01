Pick = int(input("How many apples do you pick per day ? "))
Eat = int(input("How many apples do you eat per day ? "))
RemainingApples = Pick-Eat
if RemainingApples > 0:
	print(f"There are {RemainingApples} apples remaining !")
elif RemainingApples == 0:
	print("You should save some apples and not eat all you have !")
else:
	print("You can't eat more than you pick !")


