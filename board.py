'''
Name of the Program: board.py
Description: Board class is an important component for managing the game state, handling game logic and displaying the game boards.
Date of creation: 9/11/2024
'''

from ship import Ship
from tile import Tile
from util import get_board_pos

class Board:
    def __init__(self):
        ''' 
        Here, the board class is intialized. 
        This will create two 10x10 grids where one for the player's board and one for the opponent's board.
        Each grid is filled with tile objects and initializes an empty list of ships called seld.ships that will store the player's ships.  
        '''
        self.board = [[Tile() for i in range(10)] for j in range(10)]
        self.opponent_board = [[Tile() for i in range(10)] for j in range(10)]
        self.ships = []
    
    def validate_and_add_ship(self, starting_tile, orientation, ship_length):
        ''' 
        This function will validate and place ships on the player's board. 
        The input will be such that it takes the starting tile, orientation of the tiles (either H for horizontal or V for veritcal), and the length of the ship. 
        Will ensure that the inputed placement is valid so that no ships will overlap. 
        Will re-prompt the user for valid input if the placement is invalid. '''
        while True:
            try:
                x, y = get_board_pos(starting_tile)
                
                if orientation == "H":
                    tiles = self.board[x][y:y+ship_length]
                elif orientation == "V":
                    tiles = [self.board[x+k][y] for k in range(ship_length)]
                else:
                    raise Exception("Invalid orientation")
                
                if any([tile.is_ship() for tile in tiles]):
                    raise Exception("Ship blocked by pre-existing ship")
                
                ship = Ship(tiles, ship_length)
                self.ships.append(ship)
                

                for tile in tiles:
                    tile.set_ship_id(ship.get_id())
                
                break
            except Exception as e:
                print(f"Error: {e}")
                starting_tile = input("Enter a valid starting tile (e.g., B5): ")
                orientation = input("Enter a valid orientation (H or V): ")
    
    def perform_hit(self, tile):
        ''' 
        This function is for performing a hit on the player's board at the specified tile. 
        Will take the tile input and converts it to board coordinates, and will mark that tile as hit
        If a ship  occupies the tile, it will print a "hit" message and checks if the ship is destroyed or not.'''
        x, y = get_board_pos(tile)
        tile = self.board[x][y]
        tile.is_hit = True

        print()
        if tile.is_ship():
            print("** Hit a ship! **")
            ship = [ship for ship in self.ships if ship.get_id() == tile.get_ship_id()][0]
            if ship.is_destroyed():
                ship.print_destroyed_message()
            return True
        else:
            print("*--You missed!--*")
            return False

    def record_opponent_hit(self, tile, is_hit):
        '''
        This function will record the result of a hit on the opponent's board. 
        Will take the tile input and a flag indicating whether the hit was successful or not. 
        Also will mark the tile on the opponent's board as hit and will update the shps status if hit.'''
        x, y = get_board_pos(tile)
        self.opponent_board[x][y].is_hit = True
        self.opponent_board[x][y].is_ship = is_hit
    
    # is_during_game == False => for ship placement section of game
    # is_during_game == True => during the game
    def show_board(self, is_during_game):
        '''
        This function will display the board of either the player's or opponent's.
        It will print the board grid with rows and columns and indicates the ship positions with the IDs and open sea tiles with 'O'. '''
        if not is_during_game:
            self._show_single_board(self.board)
        else:
            self._show_double_board()
            
    def _show_single_board(self, board):
        print(" ||================||")
        print("=||   YOUR BOARD   ||=")
        print(" ||================||")
        print("  1 2 3 4 5 6 7 8 9 10")
        for i in range(10):
            row_label = chr(65 + i)
            print(f"{row_label} ", end="")
            for j in range(10):
                tile = board[i][j]
                print(tile.get_ship_id() if tile.is_ship() else "O", end=" ")
            print()

    def _show_double_board(self):
        ''' 
        This function will display both player's and opponent's board side by side. 
        Here, the player's board will show the ships and hits, and the opponent's board will hide it ships but will show hits and misses. 
        '''
        print("  ||==================|====|================||")
        print("==|| OPPONENT'S BOARD |====|   YOUR BOARD   ||==")
        print("  ||==================|====|================||")
        print("  1 2 3 4 5 6 7 8 9 10     1 2 3 4 5 6 7 8 9 10")
        for i in range(10):
            row_label = chr(65 + i)
            print(f"{row_label} ", end="")
            for j in range(10):
                tile = self.opponent_board[i][j]
                if tile.is_hit:
                    print("!" if tile.is_ship else "X", end=" ")
                else:
                    print("O", end=" ")
            print("   ", end="")
            print(f"{row_label} ", end="")
            for j in range(10):
                tile = self.board[i][j]
                if tile.is_hit:
                    print("!" if tile.is_ship() else "0", end=" ")
                else:
                    print(tile.get_ship_id() if tile.is_ship() else "O", end=" ")
            print()

    def are_ships_destroyed(self):
        '''
        This function will check if all the player's ships are destroyed or not. This is done by returninf True if all ships are destroyed and False if not.
        '''
        return all([ship.is_destroyed() for ship in self.ships])