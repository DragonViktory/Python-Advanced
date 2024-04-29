def find_position(symbol, matrix):
    for row in range(len(matrix)):
        if symbol in matrix[row]:
            return [row, matrix[row].index(symbol)]


def is_in_matrix(row, col, matrix):
    return row in range(len(matrix)) and col in range(len(matrix[0]))


rows = int(input())
matrix = [[x for x in input()] for _ in range(rows)]
snake_position = find_position("S", matrix)
total_foods = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    step = input()
    matrix[snake_position[0]][snake_position[1]] = '.'
    snake_position = (snake_position[0] + directions[step][0],
                      snake_position[1] + directions[step][1])

    if not is_in_matrix(snake_position[0], snake_position[1], matrix):
        print('Game over!')
        break

    current_position_symbol = matrix[snake_position[0]][snake_position[1]]
    if current_position_symbol == "B":
        matrix[snake_position[0]][snake_position[1]] = '.'
        snake_position = find_position("B", matrix)

    elif current_position_symbol == "*":
        total_foods += 1

    matrix[snake_position[0]][snake_position[1]] = "S"
    if total_foods == 10:
        print("You won! You fed the snake.")
        break

print(f'Food eaten: {total_foods}')
[print(''.join(x)) for x in matrix]

