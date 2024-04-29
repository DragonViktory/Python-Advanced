num = int(input())

primary_sum = 0
secondary_sum = 0

for row in range(num):
    line = [int(x) for x in input().split()]

    primary_sum += line[row]
    secondary_sum += line[num - row - 1]

print(abs(primary_sum - secondary_sum))