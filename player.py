'''
Name of the Program: player.py
Description: Player class consists all the necessary functionality for a player in the battleship game including maging their own board, placing ships, handling attacks, and tracking game state.
Date of creation: 9/11/2024
'''
from board import Board

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

class Player:
    def __init__(self, player_num):
        self.board = Board()
        self.player_num = player_num

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
            if col + ship_length > 10:
                raise Exception("Invalid placement. Ship goes out of bounds horizontally")
        else:
            if row + ship_length > 10:
                raise Exception("Invalid placement. Ship goes out of bounds vertically")

    def has_lost(self):
        return self.board.are_ships_destroyed()

    def place_ships(self, num_ships_per_player):
        print("-------------------------------")
        print()
        print(f"Player {self.player_num}, place your ship{'s' if num_ships_per_player > 1 else ''}!")

        self.show_board(False)

        for i in range(1, num_ships_per_player + 1):
            while True:
                try:
                    print()
                    print(f"Choose the starting tile and orientation for ship {i} with length {i}")
                    print("Starting Tile format: Row_Letter+Column_Number (e.g., B5). Orientation format: H or V (e.g., B5,V) - ", end="")
                    placement = input()

                    self._validate_placement_input(placement, i)

                    starting_tile, orientation = placement.split(",")

                    self.board.validate_and_add_ship(starting_tile, orientation, i)

                    self.show_board(False)
                    break
                except Exception as e:
                    print(f"Error: {e}. Please try again.")

    def perform_hit(self, tile):
        return self.board.perform_hit(tile)
    
    def record_opponent_hit(self, tile, is_hit):
        self.board.record_opponent_hit(tile, is_hit)

    def show_board(self, is_during_game):
        self.board.show_board(is_during_game)