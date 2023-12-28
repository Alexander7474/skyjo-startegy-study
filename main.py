import random
from typing import List
from humanStrat import *

CARD_GRID_WIDTH = 4
CARD_GRID_HEIGHT = 3

class Card():
    def __init__(self,value):
        self.isVisible = False
        self.value = value

    def getValue(self) -> int:
        return self.value
    
    def isItVisible(self) -> bool:
        return self.isVisible
    
    def setVisibility(self,b: bool):
        self.isVisible = b

class CardPile():
    def __init__(self):
        self.firstPile = []
        self.secondPile = []

        for i in range(5): self.firstPile.append(Card(-2))
        for i in range(15): self.firstPile.append(Card(0))
        for i in range(-2,13): 
            if i != -2 and i != 0:
                for j in range(10): self.firstPile.append(Card(i))
    
    def shuffle(self):
        for i in range(5): random.shuffle(self.firstPile)

    def pickLastCard(self) -> Card:
        if (len(self.firstPile) < 1):
            cardSave = self.secondPile.pop()
            self.secondPile.reverse()
            self.firstPile = self.secondPile
            for i in range(len(self.firstPile)): self.firstPile[i].isVisible = False
            self.secondPile = []
            self.secondPile.append(cardSave)

        return self.firstPile.pop()
    
    def pickLastCardFromSecond(self) -> Card:
        if len(self.secondPile) == 0: 
            print("FATAL ERROR: try to take card from secondPile but secondPile was clear")
            exit()
        return self.secondPile.pop()
    
    def showLastCardFromSecond(self) -> Card:
        return self.secondPile[-1]
    
    def addCard(self,card: Card):
        card.setVisibility(True)
        self.secondPile.append(card)

    def randomCut(self,playerNumber: list):
        firstHalf = random.randint(playerNumber*CARD_GRID_HEIGHT*CARD_GRID_WIDTH+1,len(self.firstPile))
        self.secondPile = self.firstPile[:firstHalf]
        self.firstPile = self.firstPile[firstHalf:]
        #print("Randomcut done: " + str(len(self.secondPile)) + " " + str(len(self.firstPile)))

    def remakePile(self):
        self.firstPile = self.firstPile + self.secondPile
        self.secondPile = []

    def outCard(self):
        self.secondPile.append(self.firstPile.pop())
        self.secondPile[-1].setVisibility(True)

    def getSize(self) -> list:
        return [len(self.firstPile)+len(self.secondPile),len(self.firstPile),len(self.secondPile)]

class CardGrid():
    def __init__(self):
        self.grid: List[List] = []
        for i in range(CARD_GRID_HEIGHT):
            line: List[Card] = []
            for j in range(CARD_GRID_WIDTH):
                line.append(None)
            self.grid.append(line)

    def getGrid(self) -> list:
        return self.grid
    
    def getLine(self,index: int) -> list:
        return self.grid[index]
    
    def getCard(self,lineIndex: int,cardIndex: int) -> Card:
        return self.grid[lineIndex][cardIndex]
    
    def setCard(self,card,lineIndex,cardIndex):
        self.grid[lineIndex][cardIndex] = card

    def getTotalCard(self) -> int:
        return len(self.grid)*len(self.grid[0])
    
    def isTwoCardVisible(self):
        visibleCounter = 0
        for l in self.grid:
            for c in l:
                if c.isItVisible(): visibleCounter+=1
        return visibleCounter > 1

class Player():
    def __init__(self,name: str):
        self.name = name
        self.cards = CardGrid()

    def addCard(self,card):
        find = False
        for l in range(len(self.cards.getGrid())):
            for c in range(len(self.cards.getLine(l))):
                if self.cards.getCard(l,c) == None:
                    self.cards.setCard(card,l,c)
                    find = True
                    break
            if find == True:
                break

    def getCards(self):
        return self.cards
    
    def printGrid(self):
        gridShow = (CARD_GRID_WIDTH*4*"-")+"--"
        for l in range(len(self.getCards().getGrid())):
            line = "|"
            for c in range(len(self.getCards().getLine(l))):
                if (self.getCards().getCard(l,c).isItVisible()):
                    value = str(self.getCards().getCard(l,c).getValue())
                    if len(value) == 2:
                        line += " "+value+" "
                    else:
                        line += "  "+value+" "
                else:
                    line += " ** "
            line += "|"
            gridShow += "\n"+line
        gridShow += "\n"+(CARD_GRID_WIDTH*4*"-")+"--"
        print(gridShow)

class Game():
    def __init__(self,playerList: list[Player]):
        self.playerList = playerList
        self.gameCardPile = CardPile()
        self.gameCardPile.shuffle()
        self.gameCardPile.randomCut(len(self.playerList))
        for card in range(CARD_GRID_HEIGHT*CARD_GRID_WIDTH):
            for player in self.playerList:
                player.addCard(self.gameCardPile.pickLastCardFromSecond())
        self.gameCardPile.remakePile()
        self.gameCardPile.outCard()

    def getCardPile(self):
        return self.gameCardPile
    
    def getPlayerList(self):
        return self.playerList
    
    def gamePlay(self):
        inGame = True
        while inGame:
            for player in self.playerList:
                inGame = player.play(self)
                if inGame == False: break

def main():
    players = [Human("joe")]
    game = Game(players)
    game.gamePlay()

if __name__ == "__main__":
    main()