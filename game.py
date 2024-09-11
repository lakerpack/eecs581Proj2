from player import Player

class Game:
    def __init__(self):
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.current_turn = 0
        self.num_ships_per_player = 0

    def _game_setup(self):

        num_ships_per_player=input("[Player 1 & 2] Enter number of ships per player (1-5): ")
        while not(num_ships_per_player.isdigit()) or ((1<=int(num_ships_per_player)<=5) == False):
            num_ships_per_player=input("[Player 1 & 2] That is not valid. Enter number of ships per player (1-5): ")
        self.num_ships_per_player=int(num_ships_per_player)

        self.player1.place_ships(self.num_ships_per_player)
        self.player2.place_ships(self.num_ships_per_player)
    
    def run(self):

        self._game_setup()
        cur_player = self.player1
        next_player = self.player2

        is_game_over = False

        while not is_game_over:

            next_player.show_board(True)
            # TODO: Validate input
            tile = input("Input tile: ")
            next_player.perform_hit(tile)
            
            cur_player = self.player1 if cur_player.player_num == self.player2.player_num else self.player2
            is_game_over = cur_player.has_lost()
        
        winner = self.player1 if cur_player.player_num == self.player2.player_num else self.player1
        print(f"Player {winner.player_num} has won!")
        
    def game_stats():
        pass