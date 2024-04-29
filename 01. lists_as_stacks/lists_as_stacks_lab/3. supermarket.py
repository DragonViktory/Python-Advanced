from collections import deque

names_deque = deque
COMMAND_END = "End"
COMMANd_PAID = "Paid"

while True:
    command = input()

    if command == COMMAND_END:
        print(f"{len(names_deque)} people remaining.")
        break

    elif command == COMMANd_PAID:
        while names_deque:
            print(names_deque.popleft())

    else:
        names_deque.append(command)