import pyfiglet

group_number = pyfiglet.figlet_format("G r o u p   2", font="slant")
print(group_number)

# Game rules
print("--------------------------------------------------------")

list_for_rules = ["RULES FOR TIC-TAC-TOE", "1. The game is played on a grid that is 3 by 3 squares.",
                  "2. Player can choose either to play as X or O. Players take turns putting their marks in empty squares.",
                  "3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.",
                  "4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie."]
for x in list_for_rules:
    print(x)

print("--------------------------------------------------------")


def group2_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]) + "     " + " 1 | 2 | 3")
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]) + "     " + " 4 | 5 | 6")
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]) + "     " + " 7 | 8 | 9")
    print("\t     |     |")
    print("\n")


# scoreboard
def group2_scoreboard(game_score_board):
    print("\t--------------------------------")
    print("\t           SCOREBOARD           ")
    print("\t--------------------------------")

    players = list(game_score_board.keys())
    print("\t   ", players[0], "\t    ", game_score_board[players[0]])
    print("\t   ", players[1], "\t    ", game_score_board[players[1]])

    print("\t--------------------------------\n")
    print("\n")


# player won
def check_for_win(player_pos, current_player):
    # winning combinations
    sole = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # loop to check if any winning combinations satisfied
    for x in sole:
        if all(y in player_pos[current_player] for y in x):
            return True
    return False


# check if game is draw
def check_for_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False


# Function for a single game of Tic Tac Toe
def single_game(current_player):
    # represent tictactoe table
    values = [' ' for _ in range(9)]

    # Stores the positions occupied by X and O
    player_pos = {'X': [], 'O': []}

    # Game Loop for a single game of Tic Tac Toe
    while True:
        group2_tic_tac_toe(values)

        # Try exception block for MOVE input
        try:
            print("Player ", current_player, " turn. Which box? : ", end="")
            move = int(input())
        except ValueError:
            print("Invalid input!")
            continue

        if move < 1 or move > 9:
            print("Invalid input!")
            continue

        # Check if the box is not occupied already
        if values[move - 1] != ' ':
            print("Place already filled. Try again!")
            continue
        values[move - 1] = current_player

        # Updating player positions
        player_pos[current_player].append(move)

        # Function call for checking win
        if check_for_win(player_pos, current_player):
            group2_tic_tac_toe(values)
            print("Player ", current_player, " has won the game!")
            print("\n")
            return current_player

        # Function call for checking draw game
        if check_for_draw(player_pos):
            group2_tic_tac_toe(values)
            print("It's a tie!")
            print("\n")
            return 'D'

        # Switch player moves
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


if __name__ == "__main__":

    print("Player 1")
    player1 = input("Enter your name : ")
    print("\n")

    print("Player 2")
    player2 = input("Enter your name : ")
    print("\n")

    # Stores the player who chooses X and O
    cur_player = player1

    # Stores the choice of players
    player_choice = {'X': "", 'O': ""}

    # Stores the options
    options = ['X', 'O']

    # Stores the scoreboard
    score_board = {player1: 0, player2: 0}
    group2_scoreboard(score_board)

    # loop runs until the players quit
    while True:

        # Menu
        print("-------------------------")
        print("Turn to choose for", cur_player)
        print("(1) X")
        print("(2) O")
        print("(3) Quit")
        print("-------------------------")

        # Try exception for CHOICE input
        try:
            choice = int(input())
        except ValueError:
            print("Invalid input!\n")
            continue

        # Conditions for player choice
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1

        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1

        elif choice == 3:
            print("Final Scores")
            group2_scoreboard(score_board)
            break

        else:
            print("Invalid input!\n")
        winner = single_game(options[choice - 1])

        # Edits the scoreboard according to the winner
        if winner != 'D':
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1

        group2_scoreboard(score_board)
        while True:
            try:
                number = int(input("Type 1 to play again: "))
                if number == 1:
                    print(number)
                    break
                else:
                    print("Invalid input!")
            except ValueError:
                print("Sorry I can't understand you!")
        # Switch player who chooses X or O
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1

# -----------------START GAME-----------------
