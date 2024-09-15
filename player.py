'''
Name of the Program: player.py
Description: Player class consists all the necessary functionality for a player in the battleship game including maging their own board, placing ships, handling attacks, and tracking game state.
Date of creation: 9/11/2024
'''
from board import Board

# The letter_ind_map will map the row letter (A-J) to the corresponding value (0-9) for board positioning. 
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
        ''' 
        This function will intitalize a player instance with a board and a player number. 
        Each player will have their own board and their respective player number. '''
        self.board = Board()
        self.player_num = player_num

    def _validate_placement_input(self, placement, ship_length):
        ''' 
        This function will validate the input for ship placement by ensuring that the placement string is correctly formatted 
        and checks whether the ship fits within the board. 
        Here, the placement argument is a string containing the starting tile and orientation, and ship_length argument represents the length of the ship to be places. 
        If the placement format, starting tile, or orientation is invalid, or if the ship goes out of bounds, the function will raise an exception. 
        '''
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
        '''
        This fucntion is to check if the player has lost the game. It returns Truse if all ships are destroyed and False if not. '''
        return self.board.are_ships_destroyed()

    def place_ships(self, num_ships_per_player):
        '''
        This function will allow the players to place their ships on the board y inputting the starting tile and orientation, and it validates the input and places ships one by one. 
        Here, the num_ships_per_player argument is the number of ships the player needs to place. '''
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
        ''' 
        This function will execute a hit on the player's board at the specified tile. 
        The tile argument is the tile where the hit will be performed and this function returns true if a ship is hit and false otherwise. '''
        return self.board.perform_hit(tile)
    
    def record_opponent_hit(self, tile, is_hit):
        '''
        This function records the opponent's hit on the player's board, marking whether it was a hit or a miss. 
        The is_hit argument will return true if the opponent's hit was succesful, and false if it was a miss.'''
        self.board.record_opponent_hit(tile, is_hit)

    def show_board(self, is_during_game):
        '''
        This function will display the current state of the player's board. During the game, this can include hit/miss markers. '''
        self.board.show_board(is_during_game)