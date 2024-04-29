rows, cols = [int(x) for x in input().split()]  # 4 5
matrix = [[int(x) for x in input().split()] for row in range(rows)]  # [[1, 5, 5, 2, 4], [2, 1, 4, 14, 3], [3, 7, 11, 2, 8], [4, 8, 12, 16, 4]]

max_sum = float("-inf")  # - inf
biggest_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        first_row = matrix[row][col:col + 3]
        second_row = matrix[row + 1][col:col + 3]
        third_row = matrix[row + 2][col:col + 3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if current_sum > max_sum:
            max_sum = current_sum
            biggest_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
[print(*row) for row in biggest_matrix]
