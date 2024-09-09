class Ship:
    def __init__(self, player_id, ship_len, is_destroyed):
        self.player_id = None
        self.ship_len = None
        self.is_destroyed = None


dim=10
board={
    "A":[None]*dim,
    "B":[None]*dim,
    "C":[None]*dim,
    "D":[None]*dim,
    "E":[None]*dim,
    "F":[None]*dim,
    "G":[None]*dim,
    "H":[None]*dim,
    "I":[None]*dim,
    "J":[None]*dim
}
print(board)