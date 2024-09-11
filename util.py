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

def get_board_pos(tile):
    return (letter_ind_map[tile[0]], int(tile[1:]) - 1)

def is_valid_tile(tile):

    if len(tile) != 2 or not "A" <= tile[0] <= "J" or not tile[1:].isdigit() or not 1 <= int(tile[1:]) <= 10:
        return False
    
    return True