def player_turn(board, position, player):
    board_as_str = board[0] + board[1] + board[2]
    position -= 1
    if board_as_str[position] == "#":
        board_as_str = board_as_str[:position] + player + board_as_str[position + 1:]
    else:
        print("Invalid move, try again.")
    
    board[0] = board_as_str[:3]
    board[1] = board_as_str[3:6]
    board[2] = board_as_str[6:]


def print_board(board):
    for i in board:
        print(i)

board = ["###","###","###"]
print("Start")
print()
print_board(board)
print("\nTurn 1")
player_turn(board,5,"X")
print()
print_board(board)