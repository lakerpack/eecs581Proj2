'''
Name of the Program: scoreboard.py
Description: Player class duplicate but removes any user input and automates placement. Also has 3 different modes for targetting the other board. 
Date of creation: 9/22/2024
'''

from board import Board
from tile import Tile
from util import is_valid_tile

import random
from time import sleep

letter_ind_map={
    "A":0,
    "B":1,   
    "C":2,   
    "D":3,   
    "E":4,   
    "F":5,   
    "G":6,   
    "H":7,   
    "I":8,   
    "J":9   
}

class Bot:
    def __init__(self, player_num, difficulty):
        self.board = Board()
        self.player_num = player_num
        self.difficulty = difficulty # (A) used to keep track of difficulty
        if self.difficulty == "hard": # (A) if the difficulty is hard, then we'll start keeping track of the enemy's board
            self.enemyBoard = list()
            self.currentTarget = 0 # (A) pointer for which tile to start with, starts with the first tile then increments
        '''
        (N) Variables that check if the medium bot is locked onto a ship, the last recorded hit on a tile, 
        and the list of past shots so the bot doesn't shoot spots that have been shot before when locked onto a ship
        '''
        self.targeting_ship = False 
        self.last_hit = ""
        self.past_shots = list()

    def _validate_placement_input(self, placement, ship_length):
        v1 = placement.split(",")
        if len(v1) != 2:
            raise Exception("Invalid placement format. Expected format: Row_Letter+Column_Number,Orientation (e.g., B5,H)")

        tile = v1[0]

        if len(tile) < 2 or not "A" <= tile[0] <= "J" or not tile[1:].isdigit() or not 1 <= int(tile[1:]) <= 10:
            raise Exception("Invalid starting tile. Expected format: Row_Letter+Column_Number (e.g., B5)")

        row = letter_ind_map[tile[0]]
        col = int(tile[1:])
        
        orientation = v1[1].upper()

        if orientation not in ("H", "V"):
            raise Exception("Invalid orientation. Must be 'H' for horizontal or 'V' for vertical")

        if orientation == "H":
            if col + ship_length - 1 > 10:
                raise Exception("Invalid placement. Ship goes out of bounds horizontally")
        else:
            if row + ship_length - 1 > 10:
                raise Exception("Invalid placement. Ship goes out of bounds vertically")

    def thinking(self): # (A) printing like a bot
        print("Bot opponent is thinking", end = "", flush=True)
        sleep(0.6)
        print(".", end = "", flush=True)
        sleep(0.55)
        print(".", end = "", flush=True)
        sleep(0.50)
        print(".", end = "", flush=True)
        sleep(0.45)
        print(".", end = "", flush=True)
        sleep(0.40)

    def declareChoice(self, tile): # (A) declaring what tile was chosen
        print(f" it picks {tile}")
        sleep(1)

    def has_lost(self):
        return self.board.are_ships_destroyed()

    def attackTile(self):
        if self.difficulty == "easy": # (A) if difficulty is easy then
            return chr(random.randint(ord('A'), ord('J'))) + str(random.randint(1,10)) # return random char from A-J appended with random int from 1-10
        elif self.difficulty == "medium":
            '''
            (N) Dictating how the bot will attack if it is a medium bot. Looking to see if a tile has been hit last turn based on the targeting_ship variable. 
            If that is the case, it will shoot orthogonal tiles to the last recorded hit. 
            Will not shooting at spots that have already been shot before when shooting orthogonal tiles.
            sources: recording of orthogonal tiles partially taken from ChatGPT
            '''
            if not self.targeting_ship: #(N) if it is not targeting a ship right now then just shoot randomly
                print("picking random spot")
                return chr(random.randint(ord('A'), ord('J'))) + str(random.randint(1, 10))
            elif self.targeting_ship: #(N) if it is targeting a ship then shoot orthogonal positions to the tile
                print("locked onto a ship")
                ind_letter_map = {v: k for k, v in letter_ind_map.items()} #(N) Mapping to use the letter coordinate as an indice
                letter = self.last_hit[0] #(N) take out the letter coord and the number coord
                number = int(self.last_hit[1:]) 
                row = letter_ind_map[letter] #(N) row and column coord based on the letter and # taken out
                col = number - 1
                orthogonal_moves = [(-1, 0), (0, 1), (1, 0), (0, -1)] #(N) list of possible orthogonal tiles 
                orthogonal_positions = [] #(N) list that holds the possible orthogonal positions
                for move in orthogonal_moves: #(N) loop that creates the letter and number coordinates for the orthogonal moves to the current tile
                    new_row = row + move[0]
                    new_col = col + move[1]
                    if 0 <= new_row <= 9 and 0 <= new_col <= 9:
                        new_letter = ind_letter_map[new_row]
                        new_number = new_col + 1
                        if is_valid_tile(f"{new_letter}{new_number}"): #(N) nested if statements ensure that the shots are valid and not a tile that has already been shot
                            if f"{new_letter}{new_number}" not in self.past_shots:
                                orthogonal_positions.append(f"{new_letter}{new_number}")
                if len(orthogonal_positions) == 0: #(N) if there are not orthogonal positions left then go back to shooting randomly
                    print("out of orthogonal guesses, going back to random")
                    return chr(random.randint(ord('A'), ord('J'))) + str(random.randint(1, 10))
                print(orthogonal_positions)
                return orthogonal_positions[random.randint(0, len(orthogonal_positions) - 1)]

        elif self.difficulty == "hard": # (A) if difficulty is hard
            currentPos = self.currentTarget 
            target = self.enemyBoard[currentPos] # (A) chose target from the enemy's board
            self.currentTarget += 1 # (A) increment pointer to go next
            return target # (A) return target for the hit function

    def place_ships(self, num_ships_per_player):
        print("-------------------------------")
        print()
        print(f"The bot opponent is selecting its ship{'s' if num_ships_per_player > 1 else ''}!")
        for i in range(1, num_ships_per_player + 1):
            while True:
                try:
                    print()
                    starting_tile = chr(random.randint(ord('A'), ord('J'))) + str(random.randint(1,10)) # (A) random tile placement, random A-J and random 1-10 uses same randomness as targetting for easy
                    orientation = random.choice(['H', 'V']) # (A) pick a random orientation from H, V
                    placement = starting_tile + "," + orientation # (A) concatenate so it can be used in the placement validation
                    
                    # print(placement)
                    self._validate_placement_input(placement, i)

                    self.board.validate_and_add_ship(starting_tile, orientation, i, True)
                    print(f"Bot's ship {i} placed at {placement}.") # (A) once validated, declare where the bot has placed their tile
                    self.show_board(False) # (A) show the current board for the bot
                    break
                except Exception as e:
                    pass # (A) typically we'd have another manual input or feedback here, but for bot it'll keep repeating

    def populateEnemy(self, enemyBoard): # (A) fill up the bot's hit list if the difficulty is hard
        for i in range(len(enemyBoard.board)): # (A) iterate through all the tiles of the board
            for j in range(len(enemyBoard.board[0])):
                if enemyBoard.board[i][j].is_ship(): # (A) check if the current tile is a ship
                    self.enemyBoard.append(f"{chr(i+65)}{j+1}") # (A) use chr(i+65) to convert row to A-J

    def perform_hit(self, tile):
        return self.board.perform_hit(tile, True)
    
    def record_opponent_hit(self, tile, is_hit):
        self.board.record_opponent_hit(tile, is_hit)

    def show_board(self, is_during_game):
        self.board.show_board(is_during_game)
