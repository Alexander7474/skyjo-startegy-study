"""
ONLY LOW CARD STRATEGY
"""

from player import Player
from game import Game
from uiFonction import clearView

class onlyLowCard(Player):
    def __init__(self,name: str,maxCardValue: int):
        super().__init__(name)
        self.maxCardValue = maxCardValue

    def play(self,game: Game):
        clearView()
        print(self.name)
        if self.cards.amountNotVisibleCard() == 0:
            return False
        if not self.ready:
            self.printGrid()
            self.cards.randomInitGrid()
            self.ready = True
            return True
        else:
            self.printGrid()
            return False
        