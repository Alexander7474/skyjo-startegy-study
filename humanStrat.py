#This is the most simple startegy, like all the strategy, the class is a kid of class player and the play function is decided by player.

from main import Player,Game
import os

class Human(Player):
    def __init__(self,name: str):
        super().__init__(name)

    def play(self,game: Game):
        os.system('clear')
        if not self.cards.isTwoCardVisible():
            self.printGrid()
            print("This is you first turn, you need to return two card")
            print("First card")
            x1 = int(input('x: '))
            y1 = int(input('y: '))
            print("Second card")
            x2 = int(input('x: '))
            y2 = int(input('y: '))
            self.cards.getCard(y1-1,x1-1).setVisibility(True)
            self.cards.getCard(y2-1,x2-1).setVisibility(True)
            return True
        else:
            print('Last visible card pile: ' + str(game.getCardPile().showLastCardFromSecond().getValue()))
            print('This is your card grid: ')
            self.printGrid()
            print('What to do ?:\n1.Pick card from invisible pile\n2.Pick card from visible pile\n3.Leave')
            rep = input('-->')
            while rep != "1" and rep != "2" and rep != "3":
                print('ERROR: wrong input')
                rep = input('-->')

            if rep == "1":
                print('1')
                return True
            elif rep == "2":
                print('2')
                return True
            elif rep == "3":
                print('3')
                return False