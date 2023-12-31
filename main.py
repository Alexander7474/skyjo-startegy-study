from game import Game
from onlyLowCardStrat import onlyLowCard
from humanStrat import Human

def main():
    players = [onlyLowCard("Alex"),onlyLowCard("Paul")]
    game = Game(players)
    finalStat: dict = game.gamePlay()
    print(finalStat)

if __name__ == "__main__":
    main()