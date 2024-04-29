from functools import reduce


def add(args):
    return reduce(lambda a, b: a + b, args)


def subtract(args):
    return reduce(lambda a, b: a - b, args)


def multiply(args):
    return reduce(lambda a, b: a * b, args)


def divide(args):
    return reduce(lambda a, b: a / b, args)


mapper = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
sign = "-"
collection = [1, 2, 3]
print(mapper[sign](collection))
