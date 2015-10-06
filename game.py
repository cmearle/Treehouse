from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll


class Game:
	def setup(self):
		self.player = Character()
		self.monsters = [
			Goblin(),
			Troll(),
			Dragon()
		]
		self.monster = self.get_next_monster()

	def get_next_monster(self):
		try:
			return self.monster.pop(0)
		except IndexError:
			return None

	def monster_turn(self):
		# Check to see if the monster attacks
		# If so, tell the player
			# Check if the player wants to dodge
			# If so, see if the dodge is successful
				# If it is, move on
			# If it's not, remove one player hit point
		# If the monster isn't attacking, tell that to the player

	def player_turn(self):
		# Let the player attack, rest, or quit
		# If they attack:
			# See if the attack is succesful
				# If sok, see if the monster dodges
				#If dodged, print that
				# If not dodged, subtract the right num of hit points from the monster
			# If not a good attack, tell the player
		# If they rest:
			#Call the player.rest() method
		# If they quit:
			#Exit the game
		# If they pick anything else, re-run this method

	def clean_up(self):
		# If the monster has no more hit points
			# Up the player's experience
			# Print a message
			# Get a new monster

	def __init__(self):
		self.setup()

		while self.player.hit_points and (self.monster or self.monsters()):
			print(self.player)
			self.monster_turn()
			self.player_turn()
			self.clean_up()

		if self.player.hit_points:
			print("You win!")
		elif self.monsters or self.monster:
			print("You lose!")
