'''
Name of the Program: game.py
Description: Game class handles the main game logic including setup, turn management, and determining the winner by interacting with the player class.
Date of creation: 9/11/2024
'''
from player import Player
from bot import Bot
from scoreboard import Scoreboard
from util import is_valid_tile

import random

class Game:
    def __init__(self):
        '''This function intializes the game class by creating two players each assigned a player number i.e., 1 & 2. '''
        self.player1 = Player(1)
        self.botGame = False # (A) var to check if it's a bot game
        self.player2 = self.botCheck() or Player(2) # (A) botCheck() to ask user if they want bot, otherwise initialize player 2 
        self.scoreboard = Scoreboard() # (A) scoreboard initialization
    
    def botCheck(self):
        while True:
            answer = input("Do you wish to play against a bot? (y/n): ").lower() # (A) ask user if they want to play against a bot
            if answer == "y":
                self.botGame = True
                diff = ""
                while diff.lower() not in {"easy", "medium", "hard"}: # (A) loop until they provide a valid answer for difficulty
                    print("What difficulty level would you like?")
                    print("  -- Easy")
                    print("  -- Medium")
                    print("  -- Hard 💀")
                    diff = input().lower()
                print(" ")
                return Bot(2, diff) # (A) return the bot object with player num 2 and diff chosen
            elif answer == "n":
                return None # (A) otherwise return None so it intializes a player instead
            else:
                print("Invalid input. \n")

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
        self.scoreboard.setShips(num_ships_per_player)

        self.player1.place_ships(num_ships_per_player)
        input("Press Enter to switch to Player 2...\n")
        print()
        print()
        print()
        
        self.player2.place_ships(num_ships_per_player) # (A) will prompt the bot to choose their tiles randomly if it's a bot
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
    def _get_input_tile(self, cur_player):
        ''' 
        This function will ask the current player to input a position where they would like to attack next
        It loops until a valid position is inputed by the player. 
        By using is_valid_tile function, it ensures that the tile format is correct.
        '''
        while True:
            tile = ""
            if cur_player == self.player1 or (cur_player == self.player2 and not self.botGame):
                tile = input("Tile to attack (e.g., A1): ").strip().upper()
            elif self.botGame and cur_player == self.player2:
                tile = cur_player.attackTile()

            if is_valid_tile(tile):
                if cur_player == self.player2 and self.botGame:
                    cur_player.declareChoice(tile)
                return tile
            elif not self.botGame:
                print("Invalid input. Please enter a valid tile to attack (e.g., A1 to J10)")
    
    def run(self):
        ''' 
        This function will run the game loop.
        It starts by setting up the game and placing the ships for both players in alternate turns. 
        For each turn, the current player will attemp to hit a tile of the opponent's board. 
        The game will come to a stop when one of the player's ships are completely destroyed by the opponent.'''
        self._game_setup()
        if self.botGame and self.player2.difficulty == "hard": # (A) if the player wanted to do a hard bot
            self.player2.populateEnemy(self.player1.board) # (A) we now populate the bot's enemyboard var with their placements

        cur_player = self.player1
        next_player = self.player2
        currentOne = True # (A) scoreboard var to check which player to update/print

        is_game_over = False

        while not is_game_over:
            print(f"Player {cur_player.player_num}'s turn\n")
            cur_player.show_board(True)
            print('"X" indicates a miss, "!" indicates a hit, and ship tiles are identified by their length.')

            if cur_player == self.player2 and self.botGame: # (A) if it's a bot, we have some waiting time until they give input
                cur_player.thinking() # (A) thinking . . . 

            prev_ship_count = len([ship for ship in next_player.board.ships if not ship.is_destroyed()])

            tile = self._get_input_tile(cur_player)
            is_hit = next_player.perform_hit(tile)
            cur_player.record_opponent_hit(tile, is_hit)
            '''
            (N) basic functionality for the medium bot for recording hits and dictating the behavior to the bot class
            '''
            if cur_player == self.player2 and self.botGame and self.player2.difficulty == "medium": #(N) If the player is playing against a medium bot and it is the bot's turn
                if is_hit and tile not in self.player2.past_shots: #(N) checks for hit and if it is a hit that has not been performed before on a ship, then turn the medium bot on to shooting orthogonally to the current tile. Record current tile in last_hit
                    self.player2.last_hit = tile
                    self.player2.targeting_ship = True
                if len([ship for ship in next_player.board.ships if not ship.is_destroyed()]) < prev_ship_count: #(N) once a ship is destroyed stop targeting. Checked by comparing the previous count of ships to the current count of ships to see if the count went down.
                    self.player2.targeting_ship = False
                self.player2.past_shots.append(tile) #(N) the bot should add this current tile it is shooting to the list of past shots

            if is_hit: # (A) if player was hit
                if currentOne: # (A) check which player it was
                    self.scoreboard.updatePlayerOne(tile, len([ship for ship in next_player.board.ships if not ship.is_destroyed()])) # (A) validate tile and new score in scoreboard
                else:
                    self.scoreboard.updatePlayerTwo(tile, len([ship for ship in next_player.board.ships if not ship.is_destroyed()]))

            cur_player.show_board(True)
            is_game_over = next_player.has_lost()
            
            if not is_game_over: # (A) if the game isn't over then print the sccoreboard
                if currentOne:
                    self.scoreboard.printScoreBoard(1)
                else:
                    self.scoreboard.printScoreBoard(2)

                input("Press Enter to switch players...\n")
                cur_player, next_player = next_player, cur_player
                currentOne = not currentOne
        
        #winner = self.player1 if cur_player.player_num == self.player2.player_num else self.player1
        winner = cur_player
        print(f"Game Over! Player {winner.player_num} has won!\n")
