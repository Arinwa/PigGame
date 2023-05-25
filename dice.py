"""
The dice class for generation of a random number to be
thrown for yeah roll method, which thereafter passes argument
to dice_graph() method
"""
import random


class Dice:
    """"Random number generation"""

    def __init__(self):
        """Object initialization"""
        random.seed()

    def roll(self):
        """Throw a dice and return the face value."""
        roll = random.randint(1, 6)
        return roll

    def dice_graph(self, rep):
        """Produce graphical representation of current dice's face"""
        if rep == 1:
            print(" _______\n|       |\n|   O   |\n|_______|\n")
        elif rep == 2:
            print(" _______\n| O     |\n|       |\n|_____O_|\n")
        elif rep == 3:
            print(" _______\n| O     |\n|   O   |\n|_____O_|\n")
        elif rep == 4:
            print(" _______\n| O   O |\n|       |\n|_O___O_|\n")
        elif rep == 5:
            print(" _______\n| O   O |\n|   O   |\n|_O___O_|\n")
        elif rep == 6:
            print(" _______\n| O   O |\n| O   O |\n|_O___O_|\n")
