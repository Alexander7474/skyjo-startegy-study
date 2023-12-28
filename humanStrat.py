#HUMAN STARTEGY

#This is the most simple startegy, like all the strategy, the class is a kid of class player and the play function is decided by player.

from main import Player,Game,Card,clearView

class Human(Player):
    def __init__(self,name: str):
        super().__init__(name)

    def play(self,game: Game):
        clearView()
        print(self.name)
        if self.cards.amountVisibleCard() < 2:
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
                clearView()
                print(self.name)
                cardInUse: Card = game.gameCardPile.pickLastCard()
                cardInUse.setVisibility(True)
                print("You pick up this card: "+ str(cardInUse.getValue()))
                print('This is your card grid: ')
                self.printGrid()
                print('What to do ?:\n1.Change the card with another in your grid\n2.Put the card in the visible pile and return one of your grid')
                rep = input('-->')
                while rep != "1" and rep != "2":
                    print('ERROR: wrong input')
                    rep = input('-->')
                if rep == "1":
                    clearView()
                    print(self.name)
                    print('This is your card grid: ')
                    self.printGrid()
                    print("Wich card exchange")
                    x = int(input('x: '))
                    y = int(input('y: '))
                    game.gameCardPile.addCard(self.cards.getCard(y-1,x-1))
                    self.cards.setCard(cardInUse,y-1,x-1)
                    return not self.cards.isAllCardVisible()
                elif rep == "2":
                    clearView()
                    print(self.name)
                    print('This is your card grid: ')
                    self.printGrid()
                    print("Wich card return")
                    x = int(input('x: '))
                    y = int(input('y: '))
                    self.cards.getCard(y-1,x-1).setVisibility(True)
                    game.gameCardPile.addCard(cardInUse)
                    return not self.cards.isAllCardVisible()
            elif rep == "2":
                clearView()
                print(self.name)
                cardInUse: Card = game.gameCardPile.pickLastCardFromSecond()
                print("You pick up this card: "+ str(cardInUse.getValue()))
                print('This is your card grid: ')
                self.printGrid()
                print("Wich card exchange")
                x = int(input('x: '))
                y = int(input('y: '))
                game.gameCardPile.addCard(self.cards.getCard(y-1,x-1))
                self.cards.setCard(cardInUse,y-1,x-1)
                return not self.cards.isAllCardVisible()
            elif rep == "3":
                clearView()
                print('My final message: good bye !')
                return False