data = input().split(", ")
rows = int(data[0])
cols = int(data[1])

matrix = []
for _ in range(rows):
    elements = [int(el) for el in input().split(", ")]
    matrix.append(elements)

sum_nums = 0

for row_index in range(rows):
    for cols_index in range(cols):
        sum_nums += matrix[row_index][cols_index]

print(sum_nums)
print(matrix)
