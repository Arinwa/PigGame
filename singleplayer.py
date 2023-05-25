"""
Welcome to the Singleplayer mode game!
This module is executed when a player chooses singleplayer mode.
Type help or ? to see the list of commands.
"""
import cmd
import dice
import player
import bot


class Singleplayer(cmd.Cmd):
    """Single player command processor"""
    intro = """Type help or ? to see list commands or roll for a throw.\n"""
    isprompt = True

    if isprompt:
        prompt = "(game): "

    def __init__(self):
        """Initializes the objects."""
        super().__init__()
        self.player1 = player.Player(1)  # Player1: score = 0, index = 1
        self.dice = dice.Dice()  # dice object that will call the roll() later
        self.bot = bot.Bot()  # create bot obj
        self.bot.set_bot_level()  # call set_level() to set level atribute

    def do_set_name(self, _):
        """Type "set_name" to set a new nickname"""
        self.player1.set_name()

    def do_hold(self, _):
        """Type "hold" to end your current turn, then is bot turn"""
        self.player1.score_turn = 0  # reset the score turn for player 1
        print("Now is BOT's turn")
        self.bot.bot_turn()  # call automatic bot turn

        if self.bot.reached100():  # if True, end the game
            self.do_exit(self)
        else:
            print(f"Now is {self.player1.name}'s turn")

    def do_cheat(self, _):
        """Type "cheat" to win the game instantly"""
        self.player1.cheat()
        return self.do_exit(self)

    def do_roll(self, _):
        """Type "roll" to throw the dice"""
        rolled = self.dice.roll()
        self.dice.dice_graph(rolled)

        if rolled != 1:
            self.update_score_check_winner(rolled)
        else:
            self.remove_points_switch_turn()

    def update_score_check_winner(self, arg):
        """Update player's score and check if there is a winner"""
        self.player1.update_score(arg)  # update total score
        if self.player1.is_winner():
            self.do_exit(self)

    def remove_points_switch_turn(self):
        """Reset points from current turn and switch turn"""
        self.player1.remove_points()
        self.do_hold(self)

    def do_show_scores(self, _):
        """Type 'show_scores' to show highscore table"""
        with open('singlepl_high_scores.txt', 'r') as file:
            data = file.read()
            print(data)

    def dump_high_score(self):
        """Move player's scores and data to file"""
        str0 = f"mode: {self.bot.level}"
        str1 = f"name: {self.player1.name}, score: {self.player1.score}"
        str2 = f"name: {self.bot.name}, score: {self.bot.score}"
        str3 = "-----------------------"

        with open('singlepl_high_scores.txt', 'a+') as file:
            file.write(str0 + "\n")
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
        """Leave the game and save scores to a file"""
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
