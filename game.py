from player import Player
from util import is_valid_tile

class Game:
    def __init__(self):
        '''This function intializes the game class by creating two players each assigned a player number i.e., 1 & 2. '''
        self.player1 = Player(1)
        self.player2 = Player(2)

    def _game_setup(self):
        '''
        This function wil setup the game by asking each players to choose the number of ships they want to play with. 
        The first prompt will be for the input of number of ships per player. 
        It also ensures that the user inputs a valid value which is between 1 and 5. 
        If the user enters an value out of the range, it will ask the user to input a valid input.
        Also calls the place_ships method where both players are asked to place their ships on the board. 
        '''
        num_ships_per_player = input("[Player 1 & 2 | Game Setup] Enter number of ships per player (1-5): ")
        while not num_ships_per_player.isdigit() or not (1 <= int(num_ships_per_player) <= 5):
            num_ships_per_player = input("[Player 1 & 2 | Game Setup] That is not valid. Enter number of ships per player (1-5): ")
        num_ships_per_player = int(num_ships_per_player)

        self.player1.place_ships(num_ships_per_player)
        input("Press Enter to switch to Player 2...\n")
        print()
        print()
        print()

        self.player2.place_ships(num_ships_per_player)
        input("Press Enter to start the game...\n")
        print()
        print()
        print()
    '''
    def _get_input_tile(self):
        valid_tile = False
        while not valid_tile:
            tile = input("Tile to attack (e.g., A1): ")
            valid_tile = is_valid_tile(tile)
            if not valid_tile:
                print("Invalid input. Please enter a valid tile to attack (e.g., A1): ")
        return tile
    '''
    def _get_input_tile(self):
        ''' 
        This function will ask the current player to input a position where they would like to attack next
        It loops until a valid position is inputed by the player. 
        By using is_valid_tile function, it ensures that the tile format is correct.
        '''
        while True:
            tile = input("Tile to attack (e.g., A1): ").strip().upper()
            if is_valid_tile(tile):
                return tile
            else:
                print("Invalid input. Please enter a valid tile to attack (e.g., A1 to J10)")
    
    def run(self):
         ''' 
        This function will run the game loop.
        It starts by setting up the game and placing the ships for both players in alternate turns. 
        For each turn, the current player will attemp to hit a tile of the opponent's board. 
        The game will come to a stop when one of the player's ships are completely destroyed by the opponent.'''
        self._game_setup()
        cur_player = self.player1
        next_player = self.player2

        is_game_over = False

        while not is_game_over:
            print(f"Player {cur_player.player_num}'s turn\n")
            cur_player.show_board(True)
            print('"X" indicates a miss, "!" indicates a hit, and ship tiles are identified by their length.')

            tile = self._get_input_tile()

            is_hit = next_player.perform_hit(tile)
            cur_player.record_opponent_hit(tile, is_hit)

            cur_player.show_board(True)

            is_game_over = next_player.has_lost()
            
            if not is_game_over:
                input("Press Enter to switch players...\n")
                cur_player, next_player = next_player, cur_player
        
        #winner = self.player1 if cur_player.player_num == self.player2.player_num else self.player1
        winner = cur_player
        print(f"Game Over! Player {winner.player_num} has won!\n")
        
    def game_stats():
         '''This function is a placeholder for future implementation of the game statistics which could include total turns, hit rate, accuracy etc. '''
        pass