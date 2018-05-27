from hangman import Hangman
from chosen_word import ChosenWord
from player_guess import PlayerGuess

class Game(): 
    
    def __init__(self):
        self.hangman = Hangman()
        self.chosen_word = ChosenWord()
        self.player_guess = PlayerGuess()
        self.wrong_guesses = 0
        
    def play_game(self):
        while not self.chosen_word.is_game_over():
            self.hangman.display_hangman(self.chosen_word.get_wrong_guesses())
            self.chosen_word.display_proxy_word()
            self.player_guess.display_guesses()

            # Creates a guess for the user and checks if it is valid.
            self.player_guess.get_next_guess()

            # Sees if the user's guess appears in the selected_word, updates info as necessary.
            self.chosen_word.update(self.player_guess.get_last_guess())

        self.chosen_word.game_over_condition()


if __name__ == '__main__':
    my_game = Game()
    my_game.play_game()
