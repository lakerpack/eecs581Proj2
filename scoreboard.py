'''
Name of the Program: scoreboard.py
Description: Stores score/ship sunk data and calcualtes the current score for the round. Also updates any data and validates scores.
Date of creation: 9/22/2024
'''
class Scoreboard: # (M) keep track of hits
    def __init__(self):
        self.playerOnePoints = 0 # (M) points for each player
        self.playerTwoPoints = 0

        self.playerOneShips = 0 # (M) ships sunk for each player
        self.playerTwoShips = 0

        self.origCount = 0 # (M) keeps track of the original number of ships to calculate how many ships have been sunk

        self.oneHit = set() # (M) sets to prevent duplicate hits on the same tile from adding to count
        self.twoHit = set()

    def updatePlayerOne(self, tile, enemyShips): # (M) function to update player one's data
        if tile not in self.oneHit: # (M) validate that the tile was not hit before
            self.playerOnePoints += 1 # (M) add to points 
            self.playerOneShips = self.origCount - enemyShips # (M) calculate how many ships have been sunk so far
            self.oneHit.add(tile) # (M) add to set so no duplicates in the future

    def updatePlayerTwo(self, tile, enemyShips): # (M) same reasoning as above
        if tile not in self.twoHit:
            self.playerTwoPoints += 1
            self.playerTwoShips = self.origCount - enemyShips
            self.twoHit.add(tile)

    def setShips(self, numShips): # (M) simple setter function for num of original ships
        self.origCount = numShips
    
    def printScoreBoard(self, player): # (M) stylistic printing for the game based on player's turn
        print(" ")
        if player == 1:
            print(f"===== Player One's points: {self.playerOnePoints} =====")
            print(f"===== Player One has sunk {self.playerOneShips} thus far =====")
        else:
            print(f"===== Player Two's points: {self.playerTwoPoints} =====")
            print(f"===== Player Two has sunk {self.playerTwoShips} thus far =====")
        print(f"** Player One: {self.playerOnePoints} ({self.playerOneShips}) vs Player Two: {self.playerTwoPoints} ({self.playerTwoShips}) **")
        print(" ")