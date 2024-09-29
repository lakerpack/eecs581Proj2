class Scoreboard:
    def __init__(self):
        self.playerOnePoints = 0
        self.playerTwoPoints = 0

        self.playerOneShips = 0
        self.playerTwoShips = 0

        self.origCount = 0

        self.oneHit = set()
        self.twoHit = set()

    def updatePlayerOne(self, tile, enemyShips):
        if tile not in self.oneHit:
            self.playerOnePoints += 1
            self.playerOneShips = self.origCount - enemyShips
            self.oneHit.add(tile)

    def updatePlayerTwo(self, tile, enemyShips):
        if tile not in self.twoHit:
            self.playerTwoPoints += 1
            self.playerTwoShips = self.origCount - enemyShips
            self.twoHit.add(tile)

    def setShips(self, numShips):
        self.origCount = numShips
    
    def printScoreBoard(self, player):
        print(" ")
        if player == 1:
            print(f"===== Player One's points: {self.playerOnePoints} =====")
            print(f"===== Player One has sunk {self.playerOneShips} thus far =====")
        else:
            print(f"===== Player Two's points: {self.playerTwoPoints} =====")
            print(f"===== Player Two has sunk {self.playerTwoShips} thus far =====")
        print(f"** Player One: {self.playerOnePoints} ({self.playerOneShips}) vs Player Two: {self.playerTwoPoints} ({self.playerTwoShips}) **")
        print(" ")