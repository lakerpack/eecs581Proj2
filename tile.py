'''
Name of the Program: tile.py
Description: Represents a single square in the battleship game and provides methods to manage the information in a tile.
Date of creation: 9/11/2024
'''
class Tile:
    def __init__(self):
        '''
        This function initializes tile object. Each tile can either contain part of a ship or be empty. 
        It tracks whether a ship occupies the tile through ship_id and whether the tile has been hit. '''
        self.ship_id = None
        self.is_hit = False
    
    def is_ship(self):
        '''
        Checks if the tile contains a ship.
        Returns true if a ship occupies the tile and False otherwise. '''
        return self.ship_id is not None
    
    def get_ship_id(self):
        '''
        This function returns the ID of the ship occupying the tile.
        Returns the ID of the ship on the tile, or None if no ship is present on the tile. '''
        return self.ship_id
    
    def set_ship_id(self, ship_id):
        '''
        This function assigns a ship ID to the tile, hence marking it as occupied by a specific ship. '''
        self.ship_id = ship_id
    
    def set_is_hit(self, is_hit):
        '''
        This function marks whether the tile has been hit in the game. '''
        self.is_hit = is_hit
