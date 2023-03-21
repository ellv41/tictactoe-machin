from function import *

player = PLAYER1
while True:
    print(LOGO)
    game_over = False
    opponent1 = input("for first opponent computer press C : ").upper()
    opponent2 = input("for first opponent computer press C : ").upper()
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
