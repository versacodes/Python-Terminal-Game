# The Adventure Game

# Entity class is made for Player and Enemy to inherit the same variables and methods
class Entity:
	
	def __init__(self, name, hp, damage, items, is_defending=False):
		self.name = name
		self.hp = hp
		self.damage = damage
		self.items = items
		self.is_defending = is_defending
		
	def getinfo(self):
		return f"Name: {self.name} | Health: {self.hp} | Damage: {self.damage} | Items: {self.items}"
		
	def is_alive(self):
		if self.hp < 0:
			return False
		return True
	
	def attack(self, target):
		if target.hp > 0:
			target.hp -= self.damage
			return f"{self.name} dealt {self.damage} damage to {target.name}!"
			
# player inherits from Entity and made unique variable 'job' 
class Player(Entity):
	def __init__(self, name, hp, damage, items, job):
		super().__init__(name, hp, damage, items)
		self.job = job

# enemy inherits everything from Entity
class Enemy(Entity):
	def __init__(self, name, hp, damage, items):
		super().__init__(name, hp, damage, items)

# instantiate object
# player name is blank, ask for name by input later
player = Player("", 13, 3, {"Potion": 1}, "Warrior")
slime = Enemy("Slime", 8, 2, {})


# Title screen
print("The Adventure Game")
print("1 - Start\n2 - Quit")

# while loop checks the choice for error and its result by choice
while True:
	
	# try except if input is string
	try:
		title_screen_choice = int(input("Choose an option above: "))
	except ValueError:
		print("Enter only a number from the options above.")
		continue # resets loop
	

	if title_screen_choice == 2:
		print("Exited the game.")
		break
	# output for numbers not in given choices
	elif title_screen_choice > 2 or title_screen_choice < 1:
		print("Choose between 1 or 2 only.")

# ask for player name
player_name = input("What is your name? ")
player.name = player_name
print(f"Welcome, {player.name}. Let's begin the adventure!")
print("Which way do you want to go?")


# ask for input direction
direction_choice = int(input("1 - Forward\n2 - Left\n3 - Right\n"))

if direction_choice == 1:
	print("Going forward...")
elif direction_choice == 2:
	print("Going left...")
elif direction_choice == 3:
	print("Going right...")










