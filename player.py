"""
The player class definition.
"""
import dice


class Player:
    """"The player class"""
    score = 0
    score_turn = 0
    name = None
    player_counter = 1
    index = 0
    is_cheater = False
    is_winer = False

    def __init__(self, i):
        self.dice_obj = dice.Dice()
        self.is_winer = True
        self.is_cheater = True
        """Constructor with 'index' parameter"""
        self.index = i

    def set_name(self):
        """"Set the current name of player"""
        print(f"Set player{self.index} name:")
        self.name = input()
        print(f"Nickname for player{self.index} is set to {self.name}\n")
        return self.name

    def update_score(self, to_add):
        """Update player's overall score"""
        self.score_turn += to_add
        self.score = self.score + to_add
        print(
            f"Player {self.name} rolled {to_add}, overall score: {self.score}")

    def is_winner(self):
        """Check if a player has reached 100 points"""
        if self.score >= 100:
            print(f"\n{self.name} is the first one who reached 100 points!!")
            print(f"{self.name} WON!\n")
            return self.is_winer

    def remove_points(self):
        """Remove earned points from the current turn"""
        self.score -= self.score_turn
        print(
            (f"{self.name} rolled 1 and lost points from this turn "
             f"overall score is: {self.score}"))
        return self.score

    def cheat(self):
        """Roll dice until exceeds 100"""
        while self.score < 100:
            rolled = dice.Dice().roll()
            if rolled == 1:
                rolled += 1
            dice.Dice().dice_graph(rolled)
            self.update_score(rolled)

        print("Congrats!!! You won by cheating.")
        return self.is_cheater
