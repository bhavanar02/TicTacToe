import numpy as np
import random
import time
import matplotlib.pyplot as plt

def create_game_board():
    game_board = np.zeros((3, 3))
    return game_board

board = create_game_board()

def place_piece(board, player, position):
    if board[position] == 0:
        board[position] = player
        return board

def available_positions(board):
    empty_positions = np.where(board == 0)
    empty_positions = np.array(empty_positions)
    positions_list = list(map(tuple, np.transpose(empty_positions)))
    return positions_list

def random_place_piece(board, player):
    position = random.choice(available_positions(board))
    return place_piece(board, player, position)

board = random_place_piece(board, 2)

def check_row_win(board, player):
    for i in range(3):
        if player == board[i][0]:
            if player == board[i][1] and player == board[i][2]:
                print("True")
            else:
                print("False")
        else:
            print("False")

check_row_win(board, 1)

def check_column_win(board, player):
    for i in range(3):
        if player == board[0][i]:
            if player == board[1][i] and player == board[2][i]:
                print("True")
            else:
                print("False")
        else:
            print("False")

check_column_win(board, 1)

def check_diagonal_win(board, player):
    count = 0
    for i in range(3):
        if player == board[i][i]:
            count += 1
    if count == len(board):
        print("True")
    else:
        print("False")

check_diagonal_win(board, 1)

def game_evaluation(board):
    winner = 0
    for player in [1, 2]:
        if check_row_win(board, player) is True or check_column_win(board, player) is True:
            winner = player
        if check_diagonal_win(board, player) is True:
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

game_evaluation(board)

def play_game():
    board = create_game_board()
    if 0 in board:
        player = 1
        random_place_piece(board, player)
        game_result = game_evaluation(board)
        player = 2
    return game_result

# Plotting the results
R = 1000
results = []
start_time = time.time()
for i in range(R):
    result = play_game()
    results.append(result)

end_time = time.time()
execution_time = end_time - start_time
print(execution_time)

result_values = [results[j] for j in range(R)]
plt.hist(result_values)
plt.show()

def play_strategic_game():
    game_board, winner = create_game_board(), 0
    game_board[1, 1] = 1
    while winner == 0:
        for player in [2, 1]:
            game_board = random_place_piece(game_board, player)
            winner = game_evaluation(game_board)
            if winner != 0:
                break
    return winner

# Plotting strategic game results
R = 1000
start_time = time.time()
strategic_results = []
for i in range(R):
    strategic_result = play_strategic_game()
    strategic_results.append(strategic_result)

end_time = time.time()

strategic_values = [strategic_results[j] for j in range(R)]
plt.hist(strategic_values)
plt.show()