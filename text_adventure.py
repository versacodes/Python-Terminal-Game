# The Adventure Game

print("The Adventure Game")
print("1 - Start\n2 - Quit")

while True:
	try:
		title_screen_choice = int(input("Choose an option above: "))
	except ValueError:
		print("Enter only a number from the options above.")
		continue
	break

	if title_screen_choice == 2:
		print("Exited the game.")
	elif title_screen_choice > 2 or title_screen_choice < 1:
		print("Choose between 1 or 2 only.")

player_name = input("What is your name? ")
print(f"Welcome, {player_name}. Let's begin the adventure!")
