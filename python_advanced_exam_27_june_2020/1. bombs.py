from collections import deque

bomb_effect = deque(map(int, input().split(", ")))
bomb_casing = list(map(int, input().split(", ")))
dictionary = {
    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs",
}

dictionary_one = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}
bombs_counter = 0
created_bombs = False

while bomb_casing and bomb_effect:
    first_bomb_effect = bomb_effect[0]
    last_bomb_casing = bomb_casing[-1]
    mixes_bombs = first_bomb_effect + last_bomb_casing

    if mixes_bombs in dictionary:
        dictionary_one[dictionary[mixes_bombs]] += 1
        bomb_effect.popleft()
        bomb_casing.pop()
    else:
        bomb_casing[-1] -= 5
    for i in dictionary_one.values():
        if i < 3:
            break
    else:
        created_bombs = True
        break

print("Bene! You have successfully filled the bomb pouch!") if created_bombs else print(
    "You don't have enough materials to fill the bomb pouch.")

print("Bomb Effects: empty") if not bomb_effect else print(f"Bomb Effects: {', '.join(map(str, bomb_effect))}")
print("Bomb Casings: empty") if not bomb_casing else print(f"Bomb Casings: {', '.join(map(str, bomb_casing))}")

for key, value in sorted(dictionary_one.items()):
    print(f"{key}: {value}")