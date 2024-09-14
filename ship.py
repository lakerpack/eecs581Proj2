'''
Name of the Program: ship.py
Description: Represents a ship in a battleship game managing it's tiles, identity and destruction status, providing methods for game interactions.
Date of creation: 9/11/2024
'''
class Ship:
    def __init__(self, tiles, id):
        self.tiles = tiles
        self.id = id
        for tile in tiles:
            tile.set_ship_id(id)
    
    def get_id(self):
        return self.id
    
    def is_destroyed(self):
        return all([tile.is_hit for tile in self.tiles])
    
    def print_destroyed_message(self):
        print(f"***** Size {self.id} ship has been sunk! *****")