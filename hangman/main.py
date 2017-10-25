from hangman import Hangman
from chosen_word import ChosenWord
from player_guess import PlayerGuess

"""Creates the needed classes."""
my_hangman = Hangman()
my_word = ChosenWord()
player_guess = PlayerGuess()

"""Number of wrong guesses the user has entered."""
wrong_guesses = 0

while True:
	"""Displays necessary info for user such as the hangman, 
	number of wrong_guesses, previously entered guesses, etc."""
	my_hangman.display_hangman(wrong_guesses)
	my_word.dis_proxy_word()
	print("Wrong guesses: " + str(wrong_guesses))
	player_guess.display_used_guesses()
	
	"""Creates a guess for the user and checks if it is valid."""
	player_guess.create_guess()
	player_guess.check_guess()
	
	"""Sees if the user's guess appears in the selected_word, 
	updates info as necessary."""
	my_word.correct_guess(player_guess.guess)
	wrong_guesses = my_word.update_wrong_guesses(player_guess.guess, wrong_guesses)
	my_word.game_over(wrong_guesses)
	
	
