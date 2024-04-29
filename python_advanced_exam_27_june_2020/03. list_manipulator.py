def list_manipulator(*args):
    list_of_numbers = args[0]
    command = args[1]
    position = args[2]

    if command == "remove":
        if len(args) > 3:
            counter = args[-1]
            for _ in range(counter):
                if position == "end":
                    list_of_numbers.pop()
                else:
                    list_of_numbers.pop(0)
        else:
            if position == "end":
                list_of_numbers.pop()
            else:
                list_of_numbers.pop(0)

    else:
        numbers = [int(args[index]) for index in range(len(args) - 1, 2, - 1)]
        if position == "end":
            for num in reversed(numbers):
                list_of_numbers.append(num)
        else:
            for num in numbers:
                list_of_numbers.insert(0, num)

    return list_of_numbers


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))