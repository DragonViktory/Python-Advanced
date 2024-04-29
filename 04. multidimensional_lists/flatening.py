# matrix = [[1, 2, 3], [4, 5, 6]]
# flattened = [num for sublist in matrix for num in sublist]
# print(flattened)

matrix = [[1, 2, 3], [4, 5, 6]]

flattened = []
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        flattened.append(matrix[row][col])

for row in matrix:
    for el in matrix:
        flattened.append(el)
print(flattened)