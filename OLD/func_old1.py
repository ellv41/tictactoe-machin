import random
import pandas as pd

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
# VICTORY_X = [0, 0, 0, 0, 0, 0, 0, 0]
# VICTORY_O = [0, 0, 0, 0, 0, 0, 0, 0]
PLAYER1 = 'X'
PLAYER2 = 'O'
SIZE = ['0', '1', '2']
COMPUTER = 'C'
HUMAN = 'H'
FREE_SPC = '_'

LOGO = """
************* PLAY ******************
******** TIC   TAC   TOE ************  """


def grade_moves(match_win):
    global DATA_SET
    global GAME_DATA
    if match_win == PLAYER1:
        grade = 3
    elif match_win == PLAYER2:
        grade = -1
    else:
        grade = 1
    for i in range(0, len(GAME_DATA)):
        GAME_DATA[i][2] += grade
    if len(DATA_SET) == 0:
        DATA_SET = GAME_DATA.copy()
    else:
        for i_g in range(0, len(GAME_DATA)):
            state_found = False
            for i_d in range(0, len(DATA_SET)):
                if GAME_DATA[i_g][0:2] == DATA_SET[i_d][0:2]:
                    state_found = True
                    DATA_SET[i_d][2] += GAME_DATA[i_g][2]
            if state_found == False:
                DATA_SET.append(GAME_DATA[i_g])
    print(f'data set = {DATA_SET}')

    
def find_best_move():
    global DATA_SET
    global GAME_BOARD
    b_move = 0
    next_mov = -1
    if len(DATA_SET) >= len(GAME_DATA) and len(DATA_SET) > 0:
        for m1 in  DATA_SET:
            if m1[1] == GAME_BOARD and m1[2] > b_move:
                b_move = m1[2]
                next_mov = m1[0]
        if b_move < 3:
            return -1
        else:
            return next_mov
    return next_mov


def find_next_move(me):
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


def computer_play_rnd(plyer):
    global VICTORY_X
    global VICTORY_O
    global GAME_BOARD
    pos = -1
    empty = '_'
    empty_i = []
    board_s = len(GAME_BOARD)
    empty_spaces_sum = GAME_BOARD.count('_')
    for i in range(0, board_s):
        if GAME_BOARD[i] == empty:
            empty_i.append(i)
    pos = find_next_move(plyer)
    if pos == -1:
        pos = random.choice(empty_i)
    # print(f'pos {pos}')
    if player == PLAYER1 and len(DATA_SET) >= len(GAME_DATA):
        t_pos = find_best_move()
        if t_pos > -1:
            pos = t_pos
    return pos


def check_board(ply1):
    global VICTORY_X
    global VICTORY_O
    global GAME_BOARD
    global GAME_STATUS_MAP
    global GAME_STATUS_VAL
    # victory = [0, 0, 0, 0, 0, 0, 0, 0]
    # check cuent player squres in a row  in a col etc
    # for i in range(0, 3):
    #     victory[i] = GAME_BOARD[i*3:i*3+3].count(ply1)
    #     victory[i+3] = GAME_BOARD[i::3].count(ply1)
    # check for 2 diagonals for curent player   
    # victory[6] = GAME_BOARD[0::4].count(ply1)
    # victory[7] = GAME_BOARD[2:7:2].count(ply1)
    for id1 in range(0, 9):
        for i in range(0, 8):
            for j in range(0, 3):
                # print(f' GAME_BOARD[id1 = {GAME_BOARD[id1]}')
                if GAME_STATUS_MAP[i][j] == id1:
                    # print(f'{i}:{GAME_BOARD[id1]}')
                    GAME_STATUS_VAL[i][j] = GAME_BOARD[id1]
    # print(GAME_STATUS_VAL)
    # print(f'status for {ply1} = {victory}')
    for v1 in range(0, 8):
        if GAME_STATUS_VAL[v1].count(PLAYER1) >= 3:
            return PLAYER1 
        if GAME_STATUS_VAL[v1].count(PLAYER2) >= 3:
             return PLAYER2
    if GAME_BOARD.count(FREE_SPC) == 0:
        return 'D'         
    # if ply1 == PLAYER1:
    #     VICTORY_X = victory
    # else:
    #     VICTORY_O = victory
    # if VICTORY_X.count(3) > 0:
    #     return PLAYER1
    # elif VICTORY_O.count(3) > 0:
    #     return PLAYER2
    # elif GAME_BOARD.count(FREE_SPC) == 0:
    #     return 'D'
    return 0


def play_move_comp(plyer):
    global GAME_BOARD
    legal = False
    index = -1
    free_sq = GAME_BOARD.count(FREE_SPC)
    index = computer_play_rnd(plyer)
    # pd.DataFrame(f'{index} : {GAME_BOARD} , {"grade"}:0')
    if plyer == PLAYER1:
        GAME_DATA.append([index, GAME_BOARD, 0])
        print(f'GAME_DATA =  {GAME_DATA}')
    GAME_BOARD[index] = plyer
    return check_board(plyer)


def play_move(plyer, opponent):
    global GAME_BOARD
    legal = False
    index = -1
    free_sq = GAME_BOARD.count(FREE_SPC)
    if opponent == COMPUTER and plyer == PLAYER1:
        index = computer_play_rnd(plyer)
    else:
        while not legal:
            row = input(f'select row number  0-2 : ')
            col = input(f'select col number  0-2 : ')
            if row.isnumeric() and col.isnumeric() and row in SIZE and col in SIZE:
                index = (int(row) * 3) + int(col)
                if GAME_BOARD[index] == '_':
                    legal = True
                else:
                    print(f'select an empty place')
            else:
                print(f'enter only numbers ({SIZE})')
                legal = False
    GAME_BOARD[index] = plyer
    return check_board(plyer)


def print_bord():
    global GAME_BOARD
    print("")
    for i in range(0, len(GAME_BOARD), 3):
        print(f'|  {GAME_BOARD[i]}  |  {GAME_BOARD[i+1]}  |  {GAME_BOARD[i+2]}  |\n')


def reset_board():
    # global VICTORY_X
    # global VICTORY_O
    global GAME_BOARD

    # for i in range(0, 8):
    #     VICTORY_X[i] = 0
    #     VICTORY_O[i] = 0

    for i in range(0, 9):
        GAME_BOARD[i] = '_'


if __name__ == "__main__":
    player = PLAYER1
    while True:
        print(LOGO)
        game_over = False
        opponent1 = input("for first opponent computer press C : ").upper()
        opponent2 = input("for first opponent computer press C : ").upper()
        # opponent1 = COMPUTER
        # opponent2 = COMPUTER
        if opponent1 != COMPUTER:
            opponent1 = HUMAN
        if opponent2 != COMPUTER:
            opponent2 = HUMAN
        # start the game first move is  played by X (C)
        reset_board()
        print_bord()
        game_status = 0
        while not game_over:
            print(f'player {player} your turn')
            if GAME_BOARD.count(FREE_SPC) > 0:
                if opponent1 == COMPUTER and opponent2 == COMPUTER:
                    game_status = play_move_comp(player)
                elif opponent1 == COMPUTER:
                    game_status = play_move(player, opponent1)
                else:
                    game_status = play_move(player, opponent2)
                if player == PLAYER1:
                    player = PLAYER2
                else:
                    player = PLAYER1
                if game_status in (PLAYER1, PLAYER2):
                    print(f'\n ****** And the Winner is ********* player-{game_status}')
                    game_over = True
            else:
                print(f'no more moves the board is full @@@@@@@ its a tie @@@@@@@@')
                game_over = True
            print_bord()
        grade_moves(game_status)
        GAME_DATA.clear()
        if player == PLAYER1:
            player = PLAYER2
        else:
            player = PLAYER1
        print(f'GAME_DATA = {GAME_DATA}')
        if input('want another game press Y : ').upper() != 'Y':
            break

# end Main
