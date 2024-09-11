from ship import Ship
from tile import Tile
from util import get_board_pos

class Board:
    def __init__(self):
        self.board = [[Tile() for i in range(10)] for j in range(10)]
        self.ships = []
    
    def validate_and_add_ship(self, starting_tile, orientation, ship_length):

        x, y = get_board_pos(starting_tile)

        
        if orientation == "H":
            tiles = self.board[x][y:y+ship_length]
        elif orientation == "V":
            tiles = [self.board[k][y] for k in range(x, x+ship_length)]
        else:
            raise Exception("Invalid orientation") 
        
        if (any([tile.is_ship() for tile in tiles])):
            raise Exception("Ship blocked by pre-existing ship")

        ship = Ship(tiles, ship_length)
        self.ships.append(ship)
    
    def perform_hit(self, tile):

        x, y = get_board_pos(tile)
        tile = self.board[x][y]
        tile.is_hit = True

        if tile.is_ship():
            print("Hit a ship!")
            ship = [ship for ship in self.ships if ship.get_id() == tile.get_ship_id()][0]
            if ship.is_destroyed():
                ship.print_destroyed_message()
        else:
            print("Your hit missed!")
    
    # is_during_game == False => for ship placement section of game
    # is_during_game == True => during the game
    def show_board(self, is_during_game):

        for row in self.board:
            for tile in row:
                if is_during_game:
                    if tile.is_hit:
                        if tile.is_ship():
                            print("!", end="")
                        else:
                            print("X", end="")
                    else:
                        print("O", end="")
                else:
                    if tile.is_ship():
                        print("X", end="")
                    else:
                        print("O", end="")
            print()
            
                    


    
    def are_ships_destroyed(self):
        return all([ship.is_destroyed() for ship in self.ships])


