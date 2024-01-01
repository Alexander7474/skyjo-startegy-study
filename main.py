from game import Game
from onlyLowCardStrat import onlyLowCard
from humanStrat import Human
from uiFonction import clearView

import random

def main():
    nGame = 10000
    nPlayers = 6
    scoreMoy = [i%1 for i in range(nPlayers)]
    nWin = [i%1 for i in range(nPlayers)]
    for g in range(1,nGame+1):
        players = [onlyLowCard("pierre",6),onlyLowCard("paul",6),onlyLowCard("jack",3),onlyLowCard("patrick",6),onlyLowCard("jean",10)]
        game = Game(players)
        finalStat: dict = game.gamePlay()
        for p in range(len(players)):
            scoreMoy[p] += finalStat["score"][players[p].getName()]
            if finalStat["classement"][0] == players[p].getName():
                nWin[p]+=1
        if g % 10 == 0:
            clearView()
            print("Avencement des parties: "+str(g/(nGame/100)))
    
    print(nWin)
    print(scoreMoy)
    for p in range(len(players)):
        scoreMoy[p] = scoreMoy[p]/nGame
        print(players[p].getName()+" à fait un score moyen de: "+str(scoreMoy[p]))
        nWin[p] = nWin[p]/(nGame/100)
        print(players[p].getName()+" à fait une moyenne de victoire de: "+str(nWin[p]))
    print(nWin)
    print(scoreMoy)


if __name__ == "__main__":
    main()