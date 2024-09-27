# Battleship Game

### Quick Start and Usage
You may play Battleship by typing ```python owo.py``` in a command line interface. This assumes you are utilizing Python version 3.12 on a Windows 11 machine.

### Overview
The Battleship is a two-player strategy game where both players secretly place ships on a 10x10 grid and take turns firing at the opponent’s ships. The goal is to sink all of the opponent’s ships first.

### Features
1. **Game Setup:**
   - **Board Size:** 10x10 grid.
     - Columns: A-J
     - Rows: 1-10
   - **Number of Ships:** Players choose between 1 and 5 ships.
     - 1 ship: 1x1
     - 2 ships: 1x1, 1x2
     - Up to 5 ships: 1x1, 1x2, 1x3, 1x4, 1x5
   - **Ship Placement:** Players secretly place and orient their ships on the board.

2. **Gameplay:**
   - Players take turns firing at a coordinate on the opponent's grid.
   - The opponent announces if it’s a "hit" or "miss."
   - Boards are updated after each shot.

3. **Destroying Ships:**
   - Ships are sunk when all spaces they occupy are hit.
   - Example: A 1x3 ship on B3, B4, B5 sinks when all these spots are hit.

4. **Player's View:**
   - Players can see their own board with ship placements and hit status.
   - Players track all shots they’ve fired and whether they were hits or misses.

5. **Game End:**
   - The game ends when one player sinks all of the opponent's ships and is declared the winner.

## Latest Update

### AI Opponents:

-   **Easy Mode**: AI fires randomly each turn.
-   **Medium Mode**: AI fires randomly until it hits a ship, then targets adjacent spaces until the ship is sunk.
-   **Hard Mode**: AI knows the location of all ships and lands a hit every turn.

### Custom Addition: Scoreboard

A new scoreboard feature has been implemented to enhance the gameplay experience. This scoreboard tracks each player's points and the number of ships they've sunk.

### Scoreboard Features:

-   **Player Points**: Tracks the points for Player One and Player Two.
-   **Ships Sunk**: Displays how many enemy ships each player has sunk during the game.

The scoreboard is updated every time a player sinks an enemy ship and can be displayed at any point during the game.

