grid = "_________"

print("---------")
print("|", grid[0], grid[1], grid[2], "|")
print("|", grid[3], grid[4], grid[5], "|")
print("|", grid[6], grid[7], grid[8], "|")
print("---------")

matrix = [[], [], []]
i = 0

for j in range(0, 9, 3):
    matrix[i].extend([grid[j], grid[j + 1], grid[j + 2]])
    i += 1

print(matrix)

for k in range(10):
    if k in [0, 2, 4, 6, 8]:
        result = "X"
    else:
        result = "O"
    move = input().split()
    if len(move) != 2 or not move[0].isdigit() or not move[1].isdigit():
        print("You should enter numbers!")
    else:
        row = int(move[0])
        col = int(move[1])
        if row < 1 or row > 3 or col < 1 or col > 3:
            print("Coordinates should be from 1 to 3!")
        elif matrix[row - 1][col - 1] != "_":
            print("This cell is occupied! Choose another one!")
        else:
            matrix[row - 1][col - 1] = result
            print("---------")
            print("|", matrix[0][0], matrix[0][1], matrix[0][2], "|")
            print("|", matrix[1][0], matrix[1][1], matrix[1][2], "|")
            print("|", matrix[2][0], matrix[2][1], matrix[2][2], "|")
            print("---------")

grid_list = [matrix[i][j] for j in range(3) for i in range(3)]

grid_first_row = grid_list[0:3]
grid_first_column = [grid_list[0], grid_list[3], grid_list[6]]
grid_first_diagonal = [grid_list[0], grid_list[4], grid_list[8]]
grid_second_row = grid_list[3:6]
grid_second_column = [grid_list[1], grid_list[4], grid_list[7]]
grid_second_diagonal = [grid_list[2], grid_list[4], grid_list[6]]
grid_third_row = grid_list[6:9]
grid_third_column = [grid_list[2], grid_list[5], grid_list[8]]

combinations = [grid_first_row, grid_first_column, grid_first_diagonal, grid_second_row, grid_second_column,
                grid_second_diagonal, grid_third_row, grid_third_column]
win = []

for i in range(8):
    if combinations[i][0] == combinations[i][1] == combinations[i][2]:
        win.append(combinations[i][0])

if "X" in win and "O" not in win:
    print("X wins")
elif "X" not in win and "O" in win:
    print("O wins")
else:
    print("Draw")