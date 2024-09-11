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
        if len(v1) not in (2,3):
            raise Exception("Invalid placement")

        tile = v1[0]

        if len(tile) != 2 or not "A" <= tile[0] <= "J" or not tile[1:].isdigit() or not 1 <= int(tile[1:]) <= 10:
            raise Exception("Invalid placement")
        
        row = letter_ind_map[tile[0]]
        col = int(tile[1:])
        
        orientation = v1[1].upper()

        if orientation not in ("H", "V"):
            raise Exception("Invalid placement")
        
        if orientation == "H":
            if col + ship_length > 10:
                raise Exception("Invalid placement")
        else:
            if row + ship_length > 10:
                raise Exception("Invalid placement")
    
    def place_ships(self, num_ships_per_player):

        print(f"Player {self.player_num} placements:")
        for i in range(1, num_ships_per_player+1):
            print("Choose (Starting Tile, Orientation) of ship {i} with length {i}")
            print("Starting Tile has format: Row_Letter+Column_Number. Orientation has format: H or V (Ex: B5,V) - ", end="")
            placement = input()

            self._validate_placement_input(placement, i)