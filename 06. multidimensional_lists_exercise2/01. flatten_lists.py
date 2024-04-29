line = input().split("|") #['1 2 3 ', '4 5 6 ', ' 7 88']

sub_list = []
for substring in line[::-1]:
    sub_list.extend(substring.split())

print(*sub_list)
