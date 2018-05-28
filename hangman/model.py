import random as r
import string

# Model for hangman game, deals with all the different actions in the game - displaying info, getting next input,
# updating info, etc.
class HangmanModel():

    def __init__(self):

        # Randomly selects a word from the dictionary file
        self.selected_word = r.choice(list(open('dictionary.txt')))

        # Creates a placeholder to represent letters in the selected_word the user hasn't yet correctly guessed
        self.proxy_word = []
        for char in self.selected_word:
            self.proxy_word.append('*')

        # Number of wrong_guesses the player has entered
        self.wrong_guesses = 0

        # List of all previously entered guesses
        self.guesses = []

    # If the user's guess is in the selected_word, reveals corresponding letters in the proxy_word
    # If user's guess ins't in the selected_word, adds 1 to the number of wrong_guesses.
    def update(self):
        letter = self.get_last_guess()
        if letter in self.selected_word:
            for pos, char in enumerate(list(self.selected_word)):
                if char == letter:
                    self.proxy_word[pos] = letter
        else:
            self.wrong_guesses += 1

    # Get user's next input, keeps asking for user input until a valid guess is entered.
    def get_next_guess(self):

        valid_chars = list(string.ascii_lowercase)
        mock_guess = ""

        while len(mock_guess) != 1 or mock_guess not in valid_chars or mock_guess in self.guesses:
            mock_guess = input('Enter a letter to guess: ').lower()

            # Checks if guess is only one digit long.
            if len(mock_guess) != 1:
                print("You can only enter a single character!")

            # Checks if guess wasn't previously entered.
            if mock_guess in self.guesses:
                print("You already tried that letter!")

            if mock_guess not in valid_chars:
                print("Invalid character!")

        self.guesses.append(mock_guess)

    def display_hangman(self):

        head = "  O  "
        midbody = "/ | \\"
        legs = " / \\ "

        if self.wrong_guesses == 0:
            print(head)
            print(midbody)
            print(legs)
        elif self.wrong_guesses == 1:
            print(head)
            print(midbody)
            print(legs[0:2])
        elif self.wrong_guesses == 2:
            print(head)
            print(midbody)
        elif self.wrong_guesses == 3:
            print(head)
            print(midbody[0:4])
        elif self.wrong_guesses == 4:
            print(head)
            print(" " + midbody[1:3])
        elif self.wrong_guesses == 5:
            print(head)

    # Returns true if one of conditions for the game ending has been reached
    def is_game_over(self):
        return self.wrong_guesses >= 6 or '*' not in self.proxy_word

    # Displays the proxy_word and instructions to the user
    def display_info(self):
        print("Guess letters to try and fill in the word!")
        print(self.proxy_word)
        print("Wrong guesses: " + str(self.wrong_guesses))
        print("You have tried " + str(self.guesses))


    # If the user's guessed wrong six times, user loses. If user guessed all the letters in selected_word, user wins.
    def game_over_condition(self):
        if self.wrong_guesses == 6:
            print("You lost!")
        elif '*' not in self.proxy_word:
            print("You win!")

        print("The word was " + str(self.selected_word) + "!")
        quit()

    # Returns wrong_guesses
    def get_wrong_guesses(self):
        return self.wrong_guesses


    # Returns the last guess the user entered
    def get_last_guess(self):
        if len(self.guesses) > 0:
            return self.guesses[-1]
