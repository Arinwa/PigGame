"""
Set the game mode of the game
Press 's' for singleplayer mode
Press 'm' for multiplayer mode
"""
import cmd
import singleplayer
import multiplayer


class ChooseGameMode(cmd.Cmd):
    """"Choose game command processor"""

    intro = ("Game modes: singleplayer(press s and enter) /"
             " multiplayer(press m and enter).\n")

    def do_s(self, _):
        """Accepts 's' argument and run "singleplayer.py" and loop in cmd"""
        singleplayer.Singleplayer().cmdloop()

    def do_m(self, _):
        """Accepts 'm' argument and run "multiplayer.py" and loop in cmd"""
        multiplayer.Multiplayer().cmdloop()
