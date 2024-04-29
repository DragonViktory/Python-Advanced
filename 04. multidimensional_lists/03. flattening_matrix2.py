rows = int(input())

matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split(", ")]
    matrix.append(elements)

print([el for row in matrix for el in row])