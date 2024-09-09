class Ship:
    def __init__(self, player_id, ship_len, is_destroyed):
        self.player_id = None
        self.ship_len = None
        self.is_destroyed = None

dim=10
letter_ind_map={
    "A":0
    "B":1   
    "C":2   
    "D":3   
    "E":4   
    "F":5   
    "G":6   
    "H":7   
    "I":8   
    "J":9   
}   

num_ships_per_player=input("[Player 1 & 2] Enter number of ships per player (1-5): ")
while not(num_ships_per_player.isdigit()) or ((1<=int(num_ships_per_player)<=5) == False):
    num_ships_per_player=input("[Player 1 & 2] That is not valid. Enter number of ships per player (1-5): ")
num_ships_per_player=int(num_ships_per_player)