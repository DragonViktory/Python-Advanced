def is_out_of_matrix(matrix, row, col):
    return row not in range(len(matrix)) or col not in range(len(matrix[0]))


def mouse_position(matrix):
    for row in range(len(matrix)):
        if "M" in matrix[row]:
            return [row, matrix[row].index("M")]


row, col = [int(x) for x in input().split(",")]

matrix = [[el for el in input()] for _ in range(row)]
cheese_counter = sum([matrix[row].count("C") for row in range(len(matrix))])
current_cheese_counter = 0
start_position = mouse_position(matrix)
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

while True:
    command = input()
    if command == "danger":
        print("Mouse will come back later!")
        break

    current_row = start_position[0] + directions[command][0]
    current_col = directions[command][1] + start_position[1]

    if is_out_of_matrix(matrix, current_row, current_col):
        print("No more cheese for tonight!")
        break

    elif matrix[current_row][current_col] == "@":
        continue
    matrix[start_position[0]][start_position[1]] = "*"

    if matrix[current_row][current_col] == "C":
        current_cheese_counter += 1
        matrix[current_row][current_col] = "M"
        if current_cheese_counter == cheese_counter:
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif matrix[current_row][current_col] == "T":
        matrix[current_row][current_col] = "M"
        print("Mouse is trapped!")
        break
    start_position = [current_row, current_col]
    matrix[current_row][current_col] = "M"



[print("".join(el)) for el in matrix]


