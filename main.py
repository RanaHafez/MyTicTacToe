import random
import numpy as np

# Choosing First Player
players = ["O", "X"]
random.shuffle(players)
# print(players)

array = np.array([
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
])


def print_array():
    """A Method That prints the array in a fancy way. """
    print("   0 | 1 | 2")
    i = 0
    for row in array:
        print(f"{i}|", end="")
        for col in row:
            print(f" {col} |", end="")
        i += 1
        print()
        print("------------")

# ----------------------- Breaking down the project ---------------------------------.
# TODO check if the diag or the hor or vertical ar the same


def check_diagonal():
    """checks if one of the diagonals is identical meaning containing the same elements"""
    first_diagonal = array.diagonal()

    if first_diagonal[0] != " " and first_diagonal[0] == first_diagonal[1] == first_diagonal[2]:
        return True

    reversed_mat = np.array([np.flip(matrix) for matrix in array])
    second_diagonal = reversed_mat.diagonal()

    if second_diagonal[0] != " " and second_diagonal[0] == second_diagonal[1] == second_diagonal[2]:
        return True
    return False


def check_horizontal():
    """checks if the rows are identical. """
    for row in array:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True
    return False


def check_vertical():
    """checks if the columns are identical."""
    for i in range(3):
        row = array[:, i]
        if row[0] != " " and row[0] == row[1] == row[2]:
            return True
    return False


def is_empty(loc):
    """checks if the availability of the location entered."""
    return True if array[loc] == " " else False


turns = 4
is_winner = False
while turns != 0:
    print_array()
    first_player_entry = input(f"Enter a place to put an {players[0]} in it?(row, col) ")
    first_player = tuple(int(x) for x in first_player_entry.split(","))

    # keep prompting the user until enters an available location
    while not is_empty(first_player):
        print_array()
        first_player_entry = input(f"Enter a place to put an {players[0]} in it?(row, col) ")
        first_player = tuple(int(x) for x in first_player_entry.split(","))

    array[first_player] = players[0]
    print_array()

    # check if there is a winner
    if check_diagonal() or check_vertical() or check_horizontal():
        print(f"User 1 who plays with {players[0]} Wins .. ")
        is_winner = True
        break

    second_player_entry = input(f"Enter a place to put an {players[1]} in it?(row, col) ")
    second_player = tuple(int(x) for x in second_player_entry.split(","))

    # keep prompting the user until enters an available location
    while not is_empty(second_player):
        print_array()
        second_player_entry = input(f"Enter a place to put an {players[1]} in it?(row, col) ")
        second_player = tuple(int(x) for x in second_player_entry.split(","))

    array[second_player] = players[1]
    print_array()
    # check if there is a winner
    if check_diagonal() or check_vertical() or check_horizontal():
        print(f"User 2 who plays with {players[1]} Wins .. ")
        is_winner = True
        break
    turns -= 1

# if all the turns are ended and there is No winner
if not is_winner:
    print("This is The Last Chance for User 1 ... ")
    print_array()
    first_player_entry = input(f"Enter a place to put an {players[0]} in it?(row, col) ")
    first_player = tuple(int(x) for x in first_player_entry.split(","))

    while not is_empty(first_player):
        print_array()
        first_player_entry = input(f"Enter a place to put an {players[0]} in it?(row, col) ")
        first_player = tuple(int(x) for x in first_player_entry.split(","))

    array[first_player] = "O"
    print_array()
    if check_diagonal() or check_vertical() or check_horizontal():
        print("User 1 Wins .. ")
        is_winner = True

# array is full and there is no winner.
if not is_winner:
    print("No One Wins .. ")
print("End Of the Game")
