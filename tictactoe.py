import random
import os

GAME_BOARD = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

DATA_SET = []
GAME_DATA = []

GAME_STATUS_VAL = [['_', '_', '_'],
                   ['_', '_', '_'],
                   ['_', '_', '_'],
                   ['_', '_', '_'],
                   ['_', '_', '_'],
                   ['_', '_', '_'],
                   ['_', '_', '_'],
                   ['_', '_', '_']]

GAME_STATUS_MAP = [[0, 1, 2],
                   [3, 4, 5],
                   [6, 7, 8],
                   [0, 3, 6],
                   [1, 4, 7],
                   [2, 5, 8],
                   [0, 4, 8],
                   [2, 4, 6]]


# the first 3 items  represent rows 1 - 3 in the board  ,  the next 3  1 - 3 columns
# the 7 position is for diagonal left to right and 8 pos for the diagonal right to left
PLAYER1 = 'X'
PLAYER2 = 'O'
SIZE = ['1', '2', '3']
COMPUTER = 'C'
HUMAN = 'H'
FREE_SPC = '_'
U_find_win_bloc = False
LOGO = """

*****  GAME OF * TIC TAC TOE *****
            X O X
            O X O
            X O O
**********************************  


"""


def grade_moves(match_win):
    global DATA_SET
    global GAME_DATA
    if match_win == PLAYER1:
        grade = 3
    elif match_win == PLAYER2:
        grade = -1
    else:
        grade = 1
    for g_dat in GAME_DATA:
        g_dat[2] += grade
    if len(DATA_SET) == 0:
        DATA_SET = GAME_DATA.copy()
    else:
        for g_Dt in GAME_DATA:
            state_found = False
            for d_set in DATA_SET:
                if g_Dt[0] == d_set[0] and g_Dt[1] == d_set[1]:
                    state_found = True
                    d_set[2] += grade
            if state_found == False:
                DATA_SET.append(g_Dt)                
        f = open("DATA_SET.txt","w")
        t_rec = ""
        for set1 in DATA_SET:
            for sq in set1[1]:
                t_rec += str(f'{sq},')    
            b_rec = t_rec[0:len(t_rec)-1]
            str_rec = str(set1[0])+"@"+b_rec+"@"+str(set1[2])+"\n"
            t_rec = ""
            b_rec = ""
            f.write(str_rec) 
        f.close()
    # [print(f'data set = {x}') for x in DATA_SET]


def find_win_bloc_move(me):
    global GAME_STATUS_VAL
    global GAME_STATUS_MAP
    if me == PLAYER1:
        him = PLAYER2
    else:
        him = PLAYER1
    move = -1
    for g1 in range(0, 8):
        if GAME_STATUS_VAL[g1].count(me) == 2 and GAME_STATUS_VAL[g1].count('_') == 1:
            move = GAME_STATUS_MAP[g1][GAME_STATUS_VAL[g1].index('_')]
            return move
    for g1 in range(0, 8):
        if GAME_STATUS_VAL[g1].count(him) == 2 and GAME_STATUS_VAL[g1].count('_') == 1:
            move = GAME_STATUS_MAP[g1][GAME_STATUS_VAL[g1].index('_')]
            return move        
    return move


def find_best_move(move_c):
    global DATA_SET
    global GAME_BOARD
    grd_move = -1
    next_mov = -1
    if len(DATA_SET) > 0:
        for m1 in  DATA_SET:
            if m1[1] == GAME_BOARD and move_c == m1[0]: # and m1[2] > grd_move:
                return m1[0] , m1[2]
    return next_mov , grd_move


def computer_play(plyer):
    global GAME_BOARD
    pos = -1
    empty_i = []
    #crate a list postions of all empty squers 
    for i in range(0, len(GAME_BOARD)):
        if GAME_BOARD[i] == FREE_SPC:
            empty_i.append(i)
    # PLAYER1 (X) will play with machine learning 
    if player == PLAYER1:            
        # if next move is a certain win or block , dont search the data base
        if U_find_win_bloc:
            pos = find_win_bloc_move(plyer)
        if pos == -1:
            grd = -10
            if len(DATA_SET) > 0:
                for spc_free in empty_i:
                    t_pos , mov_grade = find_best_move(spc_free)
                    if grd < mov_grade and t_pos != -1:
                        grd = mov_grade
                        pos = t_pos
                # if pos != -1:
                    # print(f'move grade = {grd}  pos = {pos}')        
                    # xy = input("enter")
            if pos == -1 or grd < 1:
                # if no good move found in data base , take a random move       
                pos = random.choice(empty_i)
        GAME_DATA.append([pos, GAME_BOARD.copy(), 0])
    elif player == PLAYER2:            
        # pos = find_win_bloc_move(plyer)
        if pos == -1:
            pos = random.choice(empty_i)
    return pos


def play_move(plyer, opponent):
    global GAME_BOARD
    legal = False
    index = -1
    free_sq = GAME_BOARD.count(FREE_SPC)
    if opponent == COMPUTER:
        index = computer_play(plyer)
    else:
        while not legal:
            row = input(f'select row number  1-3 : ')
            col = input(f'select col number  1-3 : ')
            if row.isnumeric() and col.isnumeric() and row in SIZE and col in SIZE:
                index = ((int(row)-1) * 3) + int(col) - 1
                if GAME_BOARD[index] == '_':
                    legal = True
                else:
                    print(f'select an empty place')
            else:
                if row in ('X', 'x') or col in ('X', 'x'):
                    return -1
                print(f'enter only numbers ({SIZE})')
                legal = False
    GAME_BOARD[index] = plyer
    return check_board(plyer)


def check_board(ply1):
    global GAME_BOARD
    global GAME_STATUS_MAP
    global GAME_STATUS_VAL
    for i in range(0, 8):
        for j in range(0, 3):
            GAME_STATUS_VAL[i][j] = GAME_BOARD[GAME_STATUS_MAP[i][j]]
    for vic in GAME_STATUS_VAL:
        if vic.count(PLAYER1) >= 3:
            return PLAYER1 
        if vic.count(PLAYER2) >= 3:
             return PLAYER2
    if GAME_BOARD.count(FREE_SPC) == 0:
        return 'Draw'         
    return 0


def print_bord():
    global GAME_BOARD
    print("")
    for i in range(0, len(GAME_BOARD), 3):
        print(f'|  {GAME_BOARD[i]}  |  {GAME_BOARD[i+1]}  |  {GAME_BOARD[i+2]}  | \n')


def reset_board():
    global GAME_BOARD
    for i in range(0, 9):
        GAME_BOARD[i] = '_'

########### main ######

if __name__ == "__main__":    
    game = 1 ; num_games = 1 ; win_x = 0
    win_O = 0 ;  no_winer = 0
    display_lvl = 3
    print('\n\n\n\n\n\n')
    print(LOGO)
    if len(DATA_SET) == 0 and os.path.exists("DATA_SET.txt"):
        f = open("DATA_SET.txt","r")
        data = f.read()
        if len(data) > 0: 
            records = data.split("\n")
            data1 = []
            for record in records:
                if len(record) > 1:
                    data1 = record.split("@")
                    bord_r = list(data1[1].split(","))
                    data1 = [int(data1[0]),bord_r,int(data1[2])]
                    DATA_SET.append(data1)
        f.close()    
        # os.remove("DATA_SET.txt")
    player = PLAYER1
    opponent1 = input("for first opponent computer press C : ").upper()
    opponent2 = input("for first opponent computer press C : ").upper()
    # opponent1 = COMPUTER
    # opponent2 = COMPUTER
    if opponent1 == COMPUTER and opponent2 == COMPUTER:
        num_games = input("enter number of games for computer : ")
        if num_games.isnumeric():
            num_games = int(num_games)
        else:
            num_games = 50    
        display_lvl = 1     
        if  num_games <= 5:
            display_lvl = 3
        elif num_games <= 10:  
            display_lvl = 2
    if opponent1 != COMPUTER:
        opponent1 = HUMAN
    if opponent2 != COMPUTER:
        opponent2 = HUMAN
    if opponent1 == COMPUTER and input("use win or block function for comp X : press Y  ").upper() == 'Y':
        U_find_win_bloc = True
    x_opens = 0
# Games loop
    while True:
        player = random.choice([PLAYER1,PLAYER2])
        # player = PLAYER1
        game_over = False
        # start the game first move is  played by X (C)
        reset_board()
        game_status = 0
        player_opens = player 
        if player == PLAYER1: x_opens += 1
# Single Game Loop        
        while not game_over:
            if display_lvl == 3:
                print_bord()
                print(f'player {player} your turn')
            if GAME_BOARD.count(FREE_SPC) > 0:
                if player == PLAYER1:
                    game_status = play_move(player, opponent1)
                    player = PLAYER2
                else:
                    game_status = play_move(player, opponent2)
                    player = PLAYER1
                if game_status in (PLAYER1, PLAYER2):
                    if game_status == PLAYER1:
                        win_x += 1
                    else:
                        win_O += 1    
                    if display_lvl == 3:    
                        print_bord()
                        print(f'\n ****** And the Winner is ********* player-{game_status}')
                    game_over = True
            else:
                if display_lvl == 3:
                    print_bord()
                    print(f'no more moves the board is full @@@@@@@ its a tie @@@@@@@@')                    
                no_winer += 1
                game_over = True
            if game_status == -1:    
                game_over = True
        grade_moves(game_status)
        GAME_DATA.clear()
        if opponent1 != COMPUTER or opponent2 != COMPUTER:
            if input('want another game press Y : ').upper() != 'Y':
                break
        else:
            if display_lvl > 1:
                print_bord()
                print(f'\n Game Winer = {game_status} - player_opens = {player_opens}')
                print('\n***********************************************************')
                print(f'       END GMAE    Game :{game} of {num_games}')
                print('***********************************************************')
            if game >= num_games:
                break
        game += 1
    print(f'\n**************** Games Sumery **************** \n\n Games Plyed = {num_games}\n')    
    print(f'X wins  =  {win_x} - x opens = {x_opens} times \nO wins  =  {win_O}\nno_winer = {no_winer}\n')        
# end Main
