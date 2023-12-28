import random

CARD_GRID_WIDTH = 4
CARD_GRID_HEIGHT = 3

CARD_GRID_HEIGHT

class Card():
    def __init__(self,value):
        self.isVisible = False
        self.value = value

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

    def pickLastCard(self):
        if (len(self.firstPile) < 1):
            cardSave = self.secondPile.pop()
            self.secondPile.reverse()
            self.firstPile = self.secondPile
            for i in range(len(self.firstPile)): self.firstPile[i].isVisible = False
            self.secondPile = []
            self.secondPile.append(cardSave)

        return self.firstPile.pop()
    
    def pickLastCardFromSecond(self):
        if len(self.secondPile) == 0: 
            print("FATAL ERROR: try to take card from secondPile but secondPile was clear")
            exit()
        return self.secondPile.pop()
    
    def addCard(self,card):
        card.isVisible = True
        self.secondPile.append(card)

    def randomCut(self,playerNumber):
        firstHalf = random.randint(playerNumber*CARD_GRID_HEIGHT*CARD_GRID_WIDTH+1,len(self.firstPile))
        print("cut position: " +str(firstHalf))
        print("Randomcut not done: " + str(len(self.secondPile)) + " " + str(len(self.firstPile)))
        self.secondPile = self.firstPile[:firstHalf]
        self.firstPile = self.firstPile[firstHalf:]
        print("Randomcut done: " + str(len(self.secondPile)) + " " + str(len(self.firstPile)))

    def remakePile(self):
        self.firstPile = self.firstPile + self.secondPile
        self.secondPile = []

    def outCard(self):
        self.secondPile.append(self.firstPile.pop())
        self.secondPile[-1].isVisible = True 

class CardGrid():
    def __init__(self):
        self.grid = []
        for i in range(CARD_GRID_HEIGHT):
            line = []
            for j in range(CARD_GRID_WIDTH):
                line.append(None)
            self.grid.append(line)

    def getGrid(self):
        return self.grid
    
    def getLine(self,index):
        return self.grid[index]
    
    def getCard(self,lineIndex,cardIndex):
        return self.grid[lineIndex][cardIndex]
    
    def setCard(self,card,lineIndex,cardIndex):
        self.grid[lineIndex][cardIndex] = card

class Player():
    def __init__(self,name):
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

class Game():
    def __init__(self,playerList):
        self.playerList = playerList
        self.gameCardPile = CardPile()
        self.gameCardPile.randomCut(len(self.playerList))
        for card in range(CARD_GRID_HEIGHT*CARD_GRID_WIDTH):
            for player in self.playerList:
                player.addCard(self.gameCardPile.pickLastCardFromSecond())
        self.gameCardPile.remakePile()
        self.gameCardPile.outCard()

def main():
    players = [Player('Joe'),Player('Danie'),Player('Mark')]
    game = Game(players)

if __name__ == "__main__":
    main()