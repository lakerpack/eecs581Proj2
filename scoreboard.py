class Scoreboard:
    def __init__(self):
        self.playerOnePoints = 0
        self.playerTwoPoints = 0

        self.playerOneShips = 0
        self.playerTwoShips = 0

        self.origCount = 0

    def updatePlayerOne(self, enemyShips):
        self.playerOnePoints += 1
        self.playerOneShips = self.origCount - enemyShips

    def updatePlayerTwo(self, enemyShips):
        self.playerTwoPoints += 1
        self.playerTwoShips = self.origCount - enemyShips

    def setShips(self, numShips):
        self.origCount = numShips
    
    def printScoreBoard(self, player):
        print(" ")
        if player == 1:
            print(f"Player One's points: {self.playerOnePoints}")
            print(f"Player One has sunk {self.playerOneShips} thus far")
        else:
            print(f"Player Two's points: {self.playerTwoPoints}")
            print(f"Player Two has sunk {self.playerTwoShips} thus far")
        print(" ")