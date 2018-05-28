from model import HangmanModel


# Controller for hangman game - controlls the logic and rules of the game by using the model class
class HangmanController:

    def __init__(self):
        self.model = HangmanModel()

    def play_game(self):
        while not self.model.is_game_over():
            self.model.display_hangman()
            self.model.display_info()
            self.model.get_next_guess()
            self.model.update()

        self.model.game_over_condition()


if __name__ == '__main__':
    controller = HangmanController()
    controller.play_game()