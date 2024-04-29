stack = []

stack.append(5)
stack.append(10)
stack.append(2)

print(stack)
print(stack.pop())

while stack:
    print(stack.pop())
    print(stack)
