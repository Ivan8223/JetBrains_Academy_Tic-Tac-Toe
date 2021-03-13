def grid(cells):
    return (f"""
---------
| {' '.join(cells[0:3])} |
| {' '.join(cells[3:6])} |
| {' '.join(cells[6:9])} |
---------
""")


def turn(cells, turn_number):
    while True:
        coordinates = [i for i in input("Enter the coordinates:").split()[:2]]

        if len(coordinates) == 2 and coordinates[0].isdigit() and coordinates[1].isdigit():
            current_cell_position = 3 * int(coordinates[0]) + int(coordinates[1]) - 4

            if not 3 >= int(coordinates[0]) >= 1 or not 3 >= int(coordinates[1]) >= 1:
                print("Coordinates should be from 1 to 3!")

            elif cells[current_cell_position] in ['X', 'O']:
                print("This cell is occupied! Choose another one!")

            else:
                cells[current_cell_position] = 'X' if turn_number % 2 != 0 else 'O'
                print(grid(cells))
                break

        else:
            print("You should enter numbers!")


def game():
    cells = list("         ")

    for turn_number in range(1, 10):
        turn(cells, turn_number)

        win_conditions = [cells[0:3], cells[3:6], cells[6:9],
                          cells[0:7:3], cells[1:8:3], cells[2:9:3],
                          cells[0:9:4], cells[2:7:2]]

        if ['X', 'X', 'X'] in win_conditions:
            print("X wins")
            break

        elif ['O', 'O', 'O'] in win_conditions:
            print("O wins")
            break

    else:
        print("Draw")


game()
