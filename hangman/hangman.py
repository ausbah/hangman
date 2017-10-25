class Hangman():
	
	def __init__(self):
		"""Creates the starting structure of a hangman"""
		
		self.head = "  O  "
		self.midbody = "/ | \\"
		self.legs = " / \\ "
		
	def display_hangman(self, value):
		"""Displays parts of the hangman depending on 
		the value of wrong_guesses"""
		
		if value == 0:
			print(self.head)
			print(self.midbody)
			print(self.legs)
		elif value == 1:
			print(self.head)
			print(self.midbody)
			print(self.legs[0:2])
		elif value == 2:
			print(self.head)
			print(self.midbody)
		elif value == 3:
			print(self.head)
			print(self.midbody[0:4])
		elif value == 4:
			print(self.head)
			print(" " + self.midbody[1:3])
		elif value == 5:
			print(self.head)
			

