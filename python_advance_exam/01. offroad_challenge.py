from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption_index = deque(int(x) for x in input().split())
quantities = deque(int(x) for x in input().split())

altitude_reached = []

for number in range(len(initial_fuel)):
    current_initial_fuel = initial_fuel.pop()
    current_consumption_index = additional_consumption_index.popleft()
    current_quantities = quantities.popleft()

    if current_initial_fuel - current_consumption_index >= current_quantities:
        altitude_reached.append(f"Altitude {number + 1}")
        print(f"John has reached: Altitude {number + 1}")
    else:
        print(f"John did not reach: Altitude {number + 1}")
        break

if len(altitude_reached) == 0:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")
elif len(altitude_reached) == 4:
    print("John has reached all the altitudes and managed to reach the top!")
else:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(altitude_reached)}")