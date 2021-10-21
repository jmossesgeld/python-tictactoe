winning_combinations = ["123", "456", "789", "147", "258", "369", "159", "357"]
player_X = []
player_O = []


def evaluate_victory(player_picks):
    for combination in winning_combinations:
        win = True
        for char in combination:
            if char not in player_picks:
                win = False
        if win:
            return (True, combination)
    return (False, None)


def init_console():
    import os
    slots = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display_board():
        os.system('cls' if os.name == 'nt' else 'clear')  # clear console
        board = f" {slots[7]} | {slots[8]} | {slots[9]}       7 | 8 | 9 \n-----------     -----------\n {slots[4]} | {slots[5]} | {slots[6]}       4 | 5 | 6 \n-----------     -----------\n {slots[1]} | {slots[2]} | {slots[3]}       1 | 2 | 3 \n"
        print(board)

    def change_colors_of_winning_combinations(combination):
        for num in combination:
            slots[int(num)] = f"\033[92m{slots[int(num)]}\033[0m"

    player_picking = "X"
    for turn in range(9):
        display_board()
        pick = input(
            f"Player {player_picking}, enter a number from 1 to 9.\n")

        while(True):
            if pick in player_X or pick in player_O:
                pick = input(
                    "Slot has been taken. Please select another number.\n")
            elif not pick.isnumeric() or int(pick) < 1 or int(pick) > 9:
                pick = input(
                    "Wrong input. Please enter a number from 1 to 9.\n")
            else:
                if player_picking == "X":
                    slots[int(pick)] = "X"
                    player_X.append(pick)
                    player_picking = "O"
                else:
                    slots[int(pick)] = "O"
                    player_O.append(pick)
                    player_picking = "X"
                break

        is_X_winning, x_combination = evaluate_victory(player_X)
        is_O_winning, o_combination = evaluate_victory(player_O)

        if is_X_winning:
            change_colors_of_winning_combinations(x_combination)
            display_board()
            input("Player X wins!")
            break
        elif is_O_winning:
            change_colors_of_winning_combinations(o_combination)
            display_board()
            input("Player O wins!")
            break
        elif turn == 8:
            input("It is a draw!")


init_console()
