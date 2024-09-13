from player import Player
from util import is_valid_tile

class Game:
    def __init__(self):
        self.player1 = Player(1)
        self.player2 = Player(2)

    def _game_setup(self):
        num_ships_per_player = input("[Player 1 & 2 | Game Setup] Enter number of ships per player (1-5): ")
        while not num_ships_per_player.isdigit() or not (1 <= int(num_ships_per_player) <= 5):
            num_ships_per_player = input("[Player 1 & 2 | Game Setup] That is not valid. Enter number of ships per player (1-5): ")
        num_ships_per_player = int(num_ships_per_player)

        self.player1.place_ships(num_ships_per_player)
        input("Press Enter to switch to Player 2...")
        print()
        print()
        print()

        self.player2.place_ships(num_ships_per_player)
        input("Press Enter to start the game...")
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
        while True:
            tile = input("Tile to attack (e.g., A1): ").strip().upper()
            if is_valid_tile(tile):
                return tile
            else:
                print("Invalid input. Please enter a valid tile to attack (e.g., A1 to J10)")
    
    def run(self):
        self._game_setup()
        cur_player = self.player1
        next_player = self.player2

        is_game_over = False

        while not is_game_over:
            print(f"\nPlayer {cur_player.player_num}'s turn")
            cur_player.show_board(True)
            print('"X" indicates a miss, "!" indicates a hit, and ship tiles are identified by their length.')

            tile = self._get_input_tile()

            is_hit = next_player.perform_hit(tile)
            cur_player.record_opponent_hit(tile, is_hit)

            cur_player.show_board(True)

            is_game_over = next_player.has_lost()
            
            if not is_game_over:
                input("Press Enter to switch players...")
                cur_player, next_player = next_player, cur_player
        
        winner = self.player1 if cur_player.player_num == self.player2.player_num else self.player1
        print(f"\nGame Over! Player {winner.player_num} has won!")
        
    def game_stats():
        pass