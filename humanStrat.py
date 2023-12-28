from main import Player,CARD_GRID_WIDTH

class Human(Player):
    def __init__(self,name):
        super().__init__(name)

    def play(self):
        super().printGrid()
        