# Path Finder
## Find the shortest path to your goal using this script
### Maze format:
+ The obstacles have to be represented by '#' symbol.
+ The passages have to be represented by an empty space (' ').
+ The maze field has to be enclosed by walls ('#') from all four sides.
+ The player (the starting point) should be represented by '@' symbol. There has to be exactly one instance of a player in a maze.
+ The exit (the ending point) should be represented by 'x' or 'X'. There has to be exactly one instance of an exit in a maze.
### How to use:
1. Update the `field` variable with a maze of your design as follows:
  + every node of the maze is a separate symbol, enclosed by quotation marks and separated by commas;
  + each row of a maze has to be enclosed by square brackets and separated by commas;
  + the whole maze (all rows together) has to be enclosed by square brackets.
2. Put the starting and ending points in the desired positions.
3. Launch the script.
Once the path is found, it will be displayed in console, represented by dots.
### Notes:
The project was suggested by: https://youtu.be/txKBWtvV99Y as well as inspired by the game [CyberCodeOnline](https://cybercodeonline.com)
