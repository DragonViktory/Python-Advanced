# my_stack = []
#
# my_stack.append(5)
# my_stack.append(10)
# my_stack.append(2)
#
# # while stack:
# #     print(stack.pop())
#
# print(my_stack[-1])

# class ExampleStack:
#     def __init__(self):
#         self.stack = []
#
#     def push_value(self, value):
#         self.stack.append(value)
#
#     def pop_value(self):
#         return self.stack.pop()
#
#     def last_value(self):
#         return self.stack[-1]
#
#
# stack = ExampleStack()
# stack.push_value(1)
# stack.push_value(2)
# stack.push_value(3)
# print(stack.last_value())

# from collections import deque
#
# example = deque()
#
# example.append(1)
# example.append(2)
# example.append(3)
# example.append(4)
# example.append(5)
#
# while example:
#     print(example.popleft())
# example
# from collections import deque
#
# example_deque = deque()
# example_stack = []
#
# for i in range(1, 6):
#     example_deque.append(i)
#     example_stack.append(i)
#
# print("Deque")
# while example_deque:
#     print(example_deque.popleft())
# print("Stack")
# while example_stack:
#     print(example_stack.pop())

from collections import deque

# example_deque = []
#
# for i in range(1, 6):
#     example_deque.append(i)
#
# print("Deque from list")
#
# while example_deque:
#     print(example_deque.pop(0))