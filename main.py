from function import *
# print(f'file name = {__name__}')
while True:
    print(LOGO)
    game_over = False
    opponent = input("for playing against the computer press C : ").upper()
    if opponent != COMPUTER:
        opponent = HUMAN
    player = PLAYER1
    # start the game first move is  played by X (C)
    reset_board()
    while not game_over:
        print(f'player {player} your turn')
        game_status = play_move(player,opponent)
        print("\n")
        print_bord()
        if player == PLAYER1:
            player = PLAYER2
        else:
            player = PLAYER1
        if game_status == 'D':
            print(f'no more moves the board is full')
            game_over = True
        elif  game_status != 0:
            print(f'\n ****** And the Winner is ********* player-{game_status}')
            game_over = True
    # GAME_BOARD.clear()
    tmp1 = input('want another game press Y : ')
    if tmp1 not in ['Y', 'y']:
        break

# end Main

