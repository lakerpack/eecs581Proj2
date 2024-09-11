class Ship:
    def __init__(self, starting_tile, length, orientation):
        self.starting_tile = starting_tile
        self.length = length
        self.orientation = orientation
        self.is_destroyed = False