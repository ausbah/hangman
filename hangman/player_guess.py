class PlayerGuess():
	"""The letters the user guesses to try and reveal the randomly
	chosen word in chosen_word."""

	def __init__(self):
		"""Placeholder for user's letter guess."""
		self.guess = ""
		"""List of all previously entered guesses"""
		self.used_guesses = []
		
	def create_guess(self):
		"""Assigns the guess variable to some letter the user inputs"""
		
		self.guess = input('Enter a letter to guess: ')
		
	def check_guess(self):
		"""Checks if the player's letter is in fact a letter.
		Keeps asking for user input until a valid guess is entered."""
		
		while True:
			"""Checks if guess is only one digit long."""
			if len(self.guess)!= 1:
				print("You can only enter a single character!")
				self.create_guess()
				continue
				
			"""Checks if guess wasn't previously entered."""
			if (self.guess in self.used_guesses):
				print("You already tried that letter! Try again!")
				self.create_guess()
				continue	
			break
		
		self.add_letter()
		
	def add_letter(self):
		"""Adds guess to used_guesses"""
		
		self.used_guesses.append(self.guess)
		
	def display_used_guesses(self):
		"""Displays the guesses the user has entered."""
		
		print("You have tried " + str(self.used_guesses))
		


			
			
