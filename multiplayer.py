"""
Welcome to the Multiplayer mode game!
This module is executed when a player chooses multiplayer mode.
Type help or ? to see the list of commands.
"""

import cmd
import dice
import player


class Multiplayer(cmd.Cmd):
    """"Multiplayer command processor"""

    turn_index = 0
    intro = """Type help or ? to see list commands or roll for a throw.\n"""
    isprompt = True

    if isprompt:
        prompt = "(game): "

    def __init__(self):
        """Initialize the objects."""
        super().__init__()
        self.dice = dice.Dice()  # dice object to call the roll() later
        self.turn_index = 1
        self.player1 = player.Player(1)  # Player1: score = 0, index = 1
        self.player2 = player.Player(2)  # Player2: score = 0, index = 2

    def do_set_name(self, _):
        """Set a nickname by typing "set_name" """
        if self.turn_index == 1:
            self.player1.set_name()
        elif self.turn_index == 2:
            self.player2.set_name()

    def do_hold(self, _):
        """Type "hold" to end your current turn"""
        if self.turn_index == 1:
            self.player1.score_turn = 0  # reset the score turn for player 1
            self.turn_index = 2  # change the index to point to object player 2
            print(f"Now is {self.player2.name}'s turn")
        elif self.turn_index == 2:
            self.player2.score_turn = 0  # reset the score turn for player 2
            self.turn_index = 1  # change the index to point to 1st obj player
            print(f"Now is {self.player1.name}'s turn")

    def do_cheat(self, _):
        """Type "cheat" to win the game instantly"""
        if self.turn_index == 1:
            self.player1.cheat()
        elif self.turn_index == 2:
            self.player2.cheat()
        return self.do_exit(self)

    def do_roll(self, _):
        """Type "roll" to throw the dice"""
        rolled = self.dice.roll()
        # pass rolled as argument to generate graphical dice face
        self.dice.dice_graph(rolled)

        if rolled != 1:
            self.update_score_check_winner(rolled)
        else:
            self.remove_points_switch_turn()

    def update_score_check_winner(self, arg):
        """Update player's score and check if there is winner"""
        if self.turn_index == 1:
            self.player1.update_score(arg)  # update total score
            if self.player1.is_winner():
                self.do_exit(self)
        elif self.turn_index == 2:
            self.player2.update_score(arg)  # update total score
            if self.player2.is_winner():
                self.do_exit(self)

    def remove_points_switch_turn(self):
        """Reset points from current turn and switch turn"""
        if self.turn_index == 1:
            self.player1.remove_points()
            self.do_hold(self)
        elif self.turn_index == 2:
            self.player2.remove_points()
            self.do_hold(self)

    def do_show_scores(self, _):
        """Type 'show_scores' to show highscore table"""
        with open('multiple_high_scores.txt', 'r') as file:
            data = file.read()
            print(data)

    def dump_high_score(self):
        """Store player's scores and data to file"""
        str1 = f"name: {self.player1.name}, score: {self.player1.score}"
        str2 = f"name: {self.player2.name}, score: {self.player2.score}"
        str3 = "-----------------------"

        with open('multiple_high_scores.txt', 'a+') as file:
            file.write(str1 + "\n")
            file.write(str2 + "\n")
            file.write(str3 + "\n")

    def do_start(self, _):
        """Start a new game"""
        print("You have started a new game.\n")
        self.__init__()

    def do_restart(self, _):
        """Type "restart" to reset the current game and start a new one."""
        print("Game has been restarted.\n")
        self.__init__()

    def do_exit(self, _):
        # pylint: disable=no-self-use
        """Leave the game and players scores into file"""
        self.dump_high_score()
        print("press any key to leave game, press 's' to start a new one")
        comand = input()
        if comand == 's':
            return self.do_start(self)
        return True

    def do_EOF(self, arg):
        # pylint: disable=invalid-name
        """Leave the game."""
        return self.do_exit(arg)
