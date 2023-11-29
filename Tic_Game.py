# Task 4

import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return True

    for col in range(3):
        if len(set(board[row][col] for row in range(3))) == 1 and board[0][col] != ' ':
            return True

    if len(set(board[i][i] for i in range(3))) == 1 and board[0][0] != ' ':
        return True

    if len(set(board[i][2 - i] for i in range(3))) == 1 and board[0][2] != ' ':
        return True

    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def get_human_move(current_player):
    while True:
        try:
            move = int(input(f"Player {current_player}, enter your move in game: (1-9): "))
            if 1 <= move <= 9:
                return (move - 1) // 3, (move - 1) % 3
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_move():
    return random.randint(0, 2), random.randint(0, 2)

def play_tic_tac_toe():
    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]


        print("Welcome to Tic Tac Toe!")
        print("---------------------START THE GAME--------------------------")
        
        player_types = ['human', 'computer']
        random.shuffle(player_types)

        for _ in range(9):
            print_board(board)
            current_player_type = player_types.pop(0)
            current_player = 'X' if current_player_type == 'human' else 'O'

            if current_player_type == 'human':
                row, col = get_human_move(current_player)
            else:
                row, col = get_computer_move()

            if board[row][col] == ' ':
                board[row][col] = current_player
                if check_winner(board):
                    print_board(board)
                    if current_player_type == 'human':
                        print(f"Player {current_player} wins! Congratulations, you win!")
                    else:
                        print(f"Player {current_player} wins!")
                    break
                elif is_board_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break
            else:
                print("Cell already occupied. Try again.")

            player_types.append(current_player_type)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing Tic Tac Toe!")


play_tic_tac_toe()
