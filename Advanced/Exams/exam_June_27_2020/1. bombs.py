def fill_bomb_pouch(created_bombs: dict):
    return all(x >= 3 for x in created_bombs.values())


from collections import deque

effects = deque([int(x) for x in input().split(', ')])
casings = [int(x) for x in input().split(', ')]

bombs = {
    'Datura Bombs': 40,
    'Cherry Bombs': 60,
    'Smoke Decoy Bombs': 120
}

created_bombs = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}

while effects and casings:
    effect = effects.popleft()
    casing = casings.pop()
    value = effect + casing
    if value == bombs['Datura Bombs']:
        created_bombs['Datura Bombs'] += 1

    elif value == bombs['Cherry Bombs']:
        created_bombs['Cherry Bombs'] += 1

    elif value == bombs['Smoke Decoy Bombs']:
        created_bombs['Smoke Decoy Bombs'] += 1
    else:
        casings.append(casing - 5)
        effects.appendleft(effect)
    if fill_bomb_pouch(created_bombs):
        break

if fill_bomb_pouch(created_bombs):
    print('Bene! You have successfully filled the bomb pouch!')
else:
    print('You don\'t have enough materials to fill the bomb pouch.')
if not effects:
    print('Bomb Effects: empty')
else:
    print(f'Bomb Effects: {", ".join([str(x) for x in effects])}')
if not casings:
    print('Bomb Casings: empty')
else:
    print(f'Bomb Casings: {", ".join([str(x) for x in casings])}')
print(f'Cherry Bombs: {created_bombs["Cherry Bombs"]}')
print(f'Datura Bombs: {created_bombs["Datura Bombs"]}')
print(f'Smoke Decoy Bombs: {created_bombs["Smoke Decoy Bombs"]}')
