# tictactoe-machin By  Eli Levy
Machin learning tic tac toe   3 X 3


if you select first oppnent = C (computer)

player X will learn by machin learning

player O will play randomely (if its the computer)


after each game the moves of this game will be graded like so:
win  +3
draw +1
loss -1 

and all moves will be stored in a file DATA_SET.txt
if a move already exist in the file , the grade will be added


the board for the game wil be kept so : GAME_BOARD = ['_', '_', '_', '_', '_', '_', '_', '_', '_']


the move will be saved in the folowing format :
1@_,_,_,_,_,_,_,_,_@-5
4@_,X,_,_,_,_,O,_,_@-1
3@_,O,X,_,_,_,O,_,_@-2
0@_,O,X,X,_,_,O,_,O@-1
8@_,_,_,_,_,_,_,_,_@10
4@_,_,_,_,_,_,_,O,X@1

(charcter @ is a speretor )

first value is the position for the next move by player X
second is a list reprisenting the Game Board before the move of player X
third value is the grade acumelated for this move 



player X will play like so :

1 find the grade for each posible move
2 get the move with the highest grade (grater the 0)
3 if no good move found in the Data Base  play random move
