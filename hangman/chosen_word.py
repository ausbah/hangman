import random 

class ChosenWord():
	"""The randomly chosen word the user tries to guess letter by letter"""
	
	def __init__(self):
		"""Randomly selects a word from a dicitonary."""
		self.selected_word = random.choice(list(open('dictionary.txt')))
		
		"""Creates a placeholder to represent letters in the 
		selected_word the user hasn't yet correctly guesses."""
		self.proxy_word = []
		for char in self.selected_word:
			self.proxy_word.append('*')
	
	def dis_proxy_word(self):
		"""Displays the proxy_word and instructions."""
		
		print("Guess letters to try and fill in the word!")
		print(self.proxy_word)
		
	def correct_guess(self, letter):
		"""If the user's guess is in the selected_word, reveals 
		corresponding letters in the proxy_word."""
		
		if letter in self.selected_word:
			for pos, char in enumerate(list(self.selected_word)):
				if char == letter:
					self.proxy_word[pos] = letter 
			return self.proxy_word
			
	def update_wrong_guesses(self, letter, num):
		"""If user's guess ins't in the selected_word, adds 1 to 
		the number of wrong_guesses."""
		
		if letter not in self.selected_word:
			num += 1
		return num
			
	def game_over(self, num):
		"""If the user's guessed wrong six times, user loses. 
		If user guessed all the letters in selected_word, user wins"""
		
		if num == 6:
			print("You lost")
			quit()
		elif '*' not in self.proxy_word:
			print("You win")
			quit()

