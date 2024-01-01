"""
ONLY LOW CARD STRATEGY
"""

import random

from player import Player
from game import Game
from card import Card

class onlyLowCard(Player):
    def __init__(self,name: str,maxCardValue: int):
        super().__init__(name)
        self.maxCardValue = maxCardValue

    def play(self,game: Game):
        if self.cards.amountNotVisibleCard() == 0:
            return False
        if not self.ready:
            self.cards.randomInitGrid()
            self.ready = True
            return True
        else:
            biggestVisibleCard = self.cards.getBiggestVisibleCard()
            if biggestVisibleCard != None and biggestVisibleCard[0] > game.getCardPile().showLastCardFromSecond().getValue():
                cardInUse: Card = game.getCardPile().pickLastCardFromSecond()
                game.getCardPile().addCard(self.cards.getCard(biggestVisibleCard[1][0],biggestVisibleCard[1][1]))
                self.cards.setCard(cardInUse,biggestVisibleCard[1][0],biggestVisibleCard[1][1])
                self.cards.checkColumn(game)
                return True
            elif game.getCardPile().showLastCardFromSecond().getValue() <= self.maxCardValue:
                cardInUse: Card = game.getCardPile().pickLastCardFromSecond()
                invisibleCard = self.cards.getInvisibleCardCoo()
                rIndex= random.randint(0,len(invisibleCard)-1)
                game.getCardPile().addCard(self.cards.getCard(invisibleCard[rIndex][0],invisibleCard[rIndex][1]))
                self.cards.setCard(cardInUse,invisibleCard[rIndex][0],invisibleCard[rIndex][1])
                self.cards.checkColumn(game)
                return True
            else:
                cardInUse: Card = game.getCardPile().pickLastCard()
                if biggestVisibleCard != None and biggestVisibleCard[0] > cardInUse.getValue():
                    game.getCardPile().addCard(self.cards.getCard(biggestVisibleCard[1][0],biggestVisibleCard[1][1]))
                    self.cards.setCard(cardInUse,biggestVisibleCard[1][0],biggestVisibleCard[1][1])
                    self.cards.checkColumn(game)
                    return True
                elif cardInUse.getValue() <= self.maxCardValue:
                    invisibleCard = self.cards.getInvisibleCardCoo()
                    rIndex= random.randint(0,len(invisibleCard)-1)
                    game.getCardPile().addCard(self.cards.getCard(invisibleCard[rIndex][0],invisibleCard[rIndex][1]))
                    self.cards.setCard(cardInUse,invisibleCard[rIndex][0],invisibleCard[rIndex][1])
                    self.cards.checkColumn(game)
                    return True
                else:
                    game.getCardPile().addCard(cardInUse)
                    invisibleCard = self.cards.getInvisibleCardCoo()
                    rIndex= random.randint(0,len(invisibleCard)-1)
                    self.cards.getCard(invisibleCard[rIndex][0],invisibleCard[rIndex][1]).setVisibility(True)
                    self.cards.checkColumn(game)
                    return True
        