from ship import Ship
from tile import Tile
from util import get_board_pos

class Board:
    def __init__(self):
        self.board = [[Tile() for i in range(10)] for j in range(10)]
        self.opponent_board = [[Tile() for i in range(10)] for j in range(10)]
        self.ships = []
    
    def validate_and_add_ship(self, starting_tile, orientation, ship_length):
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
        x, y = get_board_pos(tile)
        tile = self.board[x][y]
        tile.is_hit = True

        if tile.is_ship():
            print("Hit a ship!")
            ship = [ship for ship in self.ships if ship.get_id() == tile.get_ship_id()][0]
            if ship.is_destroyed():
                ship.print_destroyed_message()
            return True
        else:
            print("You missed!")
            return False

    def record_opponent_hit(self, tile, is_hit):
        x, y = get_board_pos(tile)
        self.opponent_board[x][y].is_hit = True
        self.opponent_board[x][y].is_ship = is_hit
    
    # is_during_game == False => for ship placement section of game
    # is_during_game == True => during the game
    def show_board(self, is_during_game):
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
                print("1" if tile.is_ship() else "O", end=" ")
            print()

    def _show_double_board(self):
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
                    print("1" if tile.is_ship() else "O", end=" ")
            print()

    def are_ships_destroyed(self):
        return all([ship.is_destroyed() for ship in self.ships])