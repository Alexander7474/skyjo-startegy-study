from player import Player
from card import CardPile,CARD_GRID_WIDTH,CARD_GRID_HEIGHT

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
    
    def gamePlay(self) -> dict:
        doesPlayerFinish = True
        #We make play all the player, stop when a player had all cards visible
        while doesPlayerFinish:
            for player in self.playerList:
                doesPlayerFinish = player.play(self)
                if doesPlayerFinish == False: break
        #make all the card visible after the last turn
        for player in self.playerList:
            player.getCards().setAllCardVisible()
            print(player.getName() + " grid:")
            player.printGrid()
        #get all stat needed for the study after the game
        statistics  = {}
        statistics["numberOfPlayer"] = len(self.playerList)
        statistics["score"] = {}
        statistics["classement"] = [self.playerList[0].getName()]
        for player in self.playerList:
            statistics["score"][player.getName()] = player.getCards().getTotalValue()
            for c in range(len(statistics["classement"])):
                if statistics["score"][player.getName()] < statistics["score"][statistics["classement"][c]]:
                    statistics["classement"].insert(c, player.getName())
            if player.getName() not in statistics["classement"]: statistics["classement"].append(player.getName())
        print('Game finished')
        return statistics