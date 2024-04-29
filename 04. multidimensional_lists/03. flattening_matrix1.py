rows = int(input())

matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split(", ")]
    matrix.append(elements)

flattened = []

for row in matrix:
    for el in row:
        flattened.append(el)

print(flattened)