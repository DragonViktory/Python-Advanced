n = int(input())

matrix = []

for row in range(n):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

print(matrix[-3][-3])