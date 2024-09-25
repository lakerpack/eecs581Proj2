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
        self.difficulty = difficulty
        if self.difficulty == "hard":
            self.enemyBoard = list()
            self.currentTarget = 0
        self.targeting_ship = False #n
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

    def thinking(self):
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

    def declareChoice(self, tile):
        print(f" it picks {tile}")
        sleep(1)

    def has_lost(self):
        return self.board.are_ships_destroyed()

    def attackTile(self):
        if self.difficulty == "easy":
            return chr(random.randint(ord('A'), ord('J'))) + str(random.randint(1,10))

        elif self.difficulty == "medium":

            if not self.targeting_ship:
                print("picking random spot")
                return chr(random.randint(ord('A'), ord('J'))) + str(random.randint(1, 10))

            elif self.targeting_ship:
                print("locked onto a ship")
                # Reverse map to go from index back to letter
                ind_letter_map = {v: k for k, v in letter_ind_map.items()}

                # Split the last_hit into letter and number
                letter = self.last_hit[0]
                number = int(self.last_hit[1:])  # Extract the numeric part of the coordinate

                # Get the index of the letter
                row = letter_ind_map[letter]
                col = number - 1  # Convert to zero-based index for easier manipulation

                # Define the four orthogonal movements (up, right, down, left)
                orthogonal_moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

                # To store the resulting orthogonal positions
                orthogonal_positions = []

                # Loop through each orthogonal move
                for move in orthogonal_moves:
                    new_row = row + move[0]
                    new_col = col + move[1]

                    # Ensure the new position is within bounds (0 <= row <= 9, 0 <= col <= 9)
                    if 0 <= new_row <= 9 and 0 <= new_col <= 9:
                        new_letter = ind_letter_map[new_row]  # Get the letter for the new row
                        new_number = new_col + 1  # Convert back to 1-based index
                        if is_valid_tile(f"{new_letter}{new_number}"):
                            if f"{new_letter}{new_number}" not in self.past_shots:
                                orthogonal_positions.append(f"{new_letter}{new_number}")
                if len(orthogonal_positions) == 0:
                    print("out of orthogonal guesses, going back to random")
                    return chr(random.randint(ord('A'), ord('J'))) + str(random.randint(1, 10))
                print(orthogonal_positions)
                return orthogonal_positions[random.randint(0, len(orthogonal_positions) - 1)]

        elif self.difficulty == "hard":
            currentPos = self.currentTarget
            target = self.enemyBoard[currentPos]
            self.currentTarget += 1
            return target

    def place_ships(self, num_ships_per_player):
        print("-------------------------------")
        print()
        print(f"The bot opponent is selecting its ship{'s' if num_ships_per_player > 1 else ''}!")
        for i in range(1, num_ships_per_player + 1):
            while True:
                try:
                    print()
                    starting_tile = chr(random.randint(ord('A'), ord('J'))) + str(random.randint(1,10))
                    orientation = random.choice(['H', 'V'])
                    placement = starting_tile + "," + orientation
                    
                    # print(placement)
                    self._validate_placement_input(placement, i)

                    self.board.validate_and_add_ship(starting_tile, orientation, i, True)
                    print(f"Bot's ship {i} placed at {placement}.")
                    self.show_board(False)
                    break
                except Exception as e:
                    pass

    def populateEnemy(self, enemyBoard):
        for i in range(len(enemyBoard.board)):
            for j in range(len(enemyBoard.board[0])):
                if enemyBoard.board[i][j].is_ship():
                    self.enemyBoard.append(f"{chr(i+65)}{j+1}")

    def perform_hit(self, tile):
        return self.board.perform_hit(tile, True)
    
    def record_opponent_hit(self, tile, is_hit):
        self.board.record_opponent_hit(tile, is_hit)

    def show_board(self, is_during_game):
        self.board.show_board(is_during_game)