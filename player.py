from card import CardGrid,CARD_GRID_WIDTH

class Player():
    def __init__(self,name: str):
        self.name = name
        self.cards = CardGrid()
        self.ready = False

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

    def getName(self):
        return self.name