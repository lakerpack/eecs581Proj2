'''
Name of the Program: util.py
Description: Provides functions for for converting board coordinates and validating player inputs.
Date of creation: 9/11/2024
'''
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
'''
def is_valid_tile(tile):

    if len(tile) != 2 or not "A" <= tile[0] <= "J" or not tile[1:].isdigit() or not 1 <= int(tile[1:]) <= 10:
        return False
    
    return True
'''
def is_valid_tile(tile):
    if len(tile) < 2 or len(tile) > 3:
        return False
    
    row = tile[0].upper()
    col = tile[1:]
    
    if row not in 'ABCDEFGHIJ':
        return False
    
    try:
        col_num = int(col)
        return 1 <= col_num <= 10
    except ValueError:
        return False