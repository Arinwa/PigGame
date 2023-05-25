"""
================================================================================
================================================================================
                            WELCOME TO THE PIG GAME!
                     Select singleplayer or multiplayer mode
             Type "roll" in order to throw the dice to collect points
                               But take note!!!
        If you throw a 1, your collected points from this round will be lost.
                  So if you don't feel like taking anymore chance:
        Type "hold" to hold your points and pass the turn to your opponent.
                    Type "help"/"?" to see all commands.
               The first to reach 100 is the WINNER of the game!
"""
import choosegamemode

if __name__ == "__main__":
    print(__doc__)
    choosegamemode.ChooseGameMode().cmdloop()
