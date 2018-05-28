import random


class ChosenWord():
    # The randomly chosen word the user tries to guess letter by letter

    def __init__(self):
        # Randomly selects a word from the dictionary file
        self.selected_word = random.choice(list(open('dictionary.txt')))

        # Creates a placeholder to represent letters in the selected_word the user hasn't yet correctly guessed
        self.proxy_word = []
        for char in self.selected_word:
            self.proxy_word.append('*')

        # Number of wrong_guesses the player has entered
        self.wrong_guesses = 0

    # Displays the proxy_word and instructions to the user
    def display_proxy_word(self):
        print("Guess letters to try and fill in the word!")
        print(self.proxy_word)
        print("Wrong guesses: " + str(self.wrong_guesses))

    # If the user's guess is in the selected_word, reveals corresponding letters in the proxy_word
    # If user's guess ins't in the selected_word, adds 1 to the number of wrong_guesses.
    def update(self, letter):
        if letter in self.selected_word:
            for pos, char in enumerate(list(self.selected_word)):
                if char == letter:
                    self.proxy_word[pos] = letter
        else:
            self.wrong_guesses += 1

    # Returns true if one of conditions for the game ending has been reached
    def is_game_over(self):
        return self.wrong_guesses >= 6 or '*' not in self.proxy_word

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
