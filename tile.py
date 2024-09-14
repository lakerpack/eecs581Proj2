'''
Name of the Program: tile.py
Description: Represents a single square in the battleship game and provides methods to manage the information in a tile.
Date of creation: 9/11/2024
'''
class Tile:
    def __init__(self):
        self.ship_id = None
        self.is_hit = False
    
    def is_ship(self):
        return self.ship_id is not None
    
    def get_ship_id(self):
        return self.ship_id
    
    def set_ship_id(self, ship_id):
        self.ship_id = ship_id
    
    def set_is_hit(self, is_hit):
        self.is_hit = is_hit
