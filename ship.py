'''
Name of the Program: ship.py
Description: Represents a ship in a battleship game managing it's tiles, identity and destruction status, providing methods for game interactions.
Date of creation: 9/11/2024
'''
class Ship:
    def __init__(self, tiles, id):
        '''
        This will intialize a ship object with a set of tiles and an ID representing the ship's size or type. 
        The tiles argument is a list of Tile objects that this ship occupies. 
        The id is an identifier for the ship, typically representing the ship's size. 
        During the initialization, the ship ID is set for each tile occupied by the ship.'''
        self.tiles = tiles
        self.id = id
        for tile in tiles:
            tile.set_ship_id(id)
    
    def get_id(self):
        '''
        This function returns the ship's ID which is the length of the ship.'''
        return self.id
    
    def is_destroyed(self):
        '''
        This function checks if the ship is completely destroyed or not. A ship will be considered destroyed when all of its tiles have been hit. 
        Returns True if all the ship's tiles have been hit, and False otherwise. '''
        return all([tile.is_hit for tile in self.tiles])
    
    def print_destroyed_message(self):
        '''
        This function prints a message indicating that the ship has been destroyed.'''
        print(f"***** Size {self.id} ship has been sunk! *****")