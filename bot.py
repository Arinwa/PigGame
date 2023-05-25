"""
Bot class definition:
Including Botd difficulties feature and
Automated turn feature
"""
import random
import dice


class Bot:
    """The robot class"""
    name = "BOT"
    level = None
    score = 0
    iterations = 0

    def __init__(self):
        self.die = dice.Dice()

    def set_bot_level(self):
        """Set the bot level difficulty during the game"""
        print("Select difficulty.\nPress 'n' for normal / 'h' for hard.")
        set_d = input()

        if set_d == "n":
            print("Difficulty set to NORMAL.\n")
            self.level = "normal"
        elif set_d == "h":
            print("Difficulty set to HARD.\n")
            self.level = "hard"
        else:
            print("Wrong input.\n")
            self.set_bot_level()

    def set_iterations(self):  # set the iterations count
        """Sets how many turns the bot will play"""
        if self.level == "normal":
            self.iterations = random.randint(2, 4)
        elif self.level == "hard":
            self.iterations = random.randint(5, 8)

    def bot_turn(self):
        """Called automaticaly to roll multiple times. The number
        of times to roll depends on the 'level' value
        """
        self.set_iterations()
        for throw in range(self.iterations):
            throw = self.die.roll()
            if throw == 1:
                throw += 1
            self.die.dice_graph(throw)
            self.score += throw
        print("BOT is holding the dice.")
        self.print_score()

    def reached100(self):
        """Checks whether bot's score has reached 100 points"""
        if self.score >= 100:
            print("BOT won the game, reached 100 points!")
            return True

    def print_score(self):
        """Print BOT's turn score"""
        print(f"BOT's score is {self.score}")
