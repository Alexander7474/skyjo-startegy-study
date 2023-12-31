import random
from typing import List

CARD_GRID_WIDTH = 4
CARD_GRID_HEIGHT = 3

class Card():
    def __init__(self,value: int):
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
    
    def setCard(self,card,lineIndex: int,cardIndex: int):
        self.grid[lineIndex][cardIndex] = card

    def getTotalCard(self) -> int:
        """
        Return the total number of card
        
        Return
        ------
            total
        """
        return len(self.grid)*len(self.grid[0])
    
    def amountVisibleCard(self) -> int:
        """
        Return the amount of card visible in player grid
        
        Return
        ------
        visibleCounter: int
            the count of visible card in player grid
        """
        visibleCounter = 0
        for l in self.grid:
            for c in l:
                if c.isItVisible(): visibleCounter+=1
        return visibleCounter
    
    def amountNotVisibleCard(self):
        """
        Return the amount of card not visible in player grid
        
        Return
        ------
        notVisibleCounter: int
            the count of not visible card in player grid
        """
        notVisibleCounter = 0
        for l in self.grid:
            for c in l:
                if not c.isItVisible(): notVisibleCounter+=1
        return notVisibleCounter
    
    def setAllCardVisible(self):
        """Set all card in the player grid visible"""
        for l in range(len(self.grid)):
            for c in range(len(self.grid[l])):
                self.grid[l][c].setVisibility(True)
    
    def getTotalValue(self) -> int:
        """
        Return the total value of all card
        
        Return
        ------
        total: int
            the total
        """
        total = 0
        for l in range(len(self.grid)):
            for c in range(len(self.grid[l])):
                total += self.grid[l][c].getValue()
        return total
    
    def checkColumn(self,game):
        """
        Search a column with all card with the same value
        
        Parameter
        ---------
        game: Game
            the game where the player is to add the card in visible pile
        """
        for c in range(len(self.grid[0])):
            equalCounter = 0
            for l in range(1,len(self.grid)):
                if self.grid[l][c].getValue() == self.grid[l-1][c].getValue():
                    equalCounter += 1
            if equalCounter == CARD_GRID_HEIGHT-1:
                for l in range(len(self.grid)):
                    game.getCardPile().addCard(self.grid[l].pop(c))
                break
    
    def getVisibleCardCoo(self) -> list[list[int]]:
        """
        Return a list with the coordinates of all visible card in player grid
        
        Return
        ------
        visibleList: list[list[int]]
            the list of coordinate
        """
        visibleList = []
        for l in range(len(self.grid)):
            for c in range(len(self.grid[l])):
                if self.grid[l][c].isItVisible(): visibleList.append([c,l])
        return visibleList
    
    def getInvisibleCardCoo(self) -> list[list[int]]:
        """
        Return a list with the coordinates of all invisible card in player grid
        
        Return
        ------
        invisibleList: list[list[int]]
            the list of coordinate
        """
        invisibleList: list[list[int]] = []
        for l in range(len(self.grid)):
            for c in range(len(self.grid[l])):
                if not self.grid[l][c].isItVisible(): invisibleList.append([c,l])
        return invisibleList
    
    def getBiggestVisibleCardCoo(self) -> list[int]:
        """
        Return the coordinate of the visible card with biggest value in player grid
        
        Return
        ------
        cardCoo: list[int]
            the coordinate of the card
        """
        cardCoo: list[int] = []
        x = -3
        for l in range(len(self.grid)):
            for c in range(len(self.grid[l])):
                if x < self.grid[l][c].getValue() and self.grid[l][c].isItVisible(): 
                    x = self.grid[l][c].getValue()
                    cardCoo = [c,l]
        return cardCoo
    
    def getSmallestVisibleCardCoo(self) -> list[int]:
        """
        Return the coordinate of the visible card with smallest value in player grid
        
        Return
        ------
        cardCoo: list[int]
            the coordinate of the card
        """
        cardCoo: list[int] = []
        x = 13
        for l in range(len(self.grid)):
            for c in range(len(self.grid[l])):
                if x > self.grid[l][c].getValue() and self.grid[l][c].isItVisible(): 
                    x = self.grid[l][c].getValue()
                    cardCoo = [c,l]
        return cardCoo
    
    def randomInitGrid(self):
        """
        Set 2 random card visible in the grid, not in the same column
        """
        x1 = random.randint(0,1)
        y1 = random.randint(0,3)
        x2 = random.randint(2,3)
        y2 = random.randint(0,3)
        self.grid[y1,x1].setVisibility(True)
        self.grid[y2,x2].setVisibility(True)