import string

class PlayerGuess():
    # The letters the user guesses to try and reveal the randomly chosen word in chosen_word."""

    def __init__(self):

        # List of all previously entered guesses
        self.guesses = []

        # List of valid characters
        self.valid_chars = list(string.ascii_lowercase)

    # Checks if the player's letter is in fact a letter. Keeps asking for user input until a valid guess is entered.
    def get_next_guess(self):

        mock_guess = ""

        while len(mock_guess) != 1 or mock_guess not in self.valid_chars or mock_guess in self.guesses:
            mock_guess = input('Enter a letter to guess: ').lower()
            
            # Checks if guess is only one digit long.
            if len(mock_guess) != 1:
                print("You can only enter a single character!")

            # Checks if guess wasn't previously entered.
            if mock_guess in self.guesses:
                print("You already tried that letter!")

            if mock_guess not in self.valid_chars:
                print("Invalid character!")

        self.guesses.append(mock_guess)

    # Returns the last guess the user entered
    def get_last_guess(self):
        if len(self.guesses) > 0:
            return self.guesses[-1]

    # Displays the guesses the user has entered.
    def display_guesses(self):
        print("You have tried " + str(self.guesses))
