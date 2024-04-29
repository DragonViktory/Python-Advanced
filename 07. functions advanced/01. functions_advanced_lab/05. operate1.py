from functools import reduce


def operate(sign, *args):
    return reduce(lambda a, b:eval(f"{a}{sign}{b}"), args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
