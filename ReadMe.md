# Battleship Game

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



