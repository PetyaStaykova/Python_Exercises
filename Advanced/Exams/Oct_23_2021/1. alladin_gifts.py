from collections import deque


def is_present_made(points: int):
    if 100 <= points <= 499:
        return True
    return False


def check_which_present_made(presents: dict, points: int):
    if 100 <= points <= 199:
        presents['Gemstone'] += 1
    elif 200 <= points <= 299:
        presents['Porcelain Sculpture'] += 1
    elif 300 <= points <= 399:
        presents['Gold'] += 1
    elif 400 <= points <= 499:
        presents['Diamond Jewellery'] += 1


materials = [int(x) for x in input().split()]
magics = deque([int(x) for x in input().split()])

presents = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}
while materials and magics:
    material = materials.pop()
    magic = magics.popleft()
    mixed = material + magic
    if mixed < 100:
        if mixed % 2 == 0:
            material *= 2
            magic *= 3
            mixed = material + magic

        else:
            material *= 2
            magic *= 2
            mixed = material + magic
        if is_present_made(mixed):
            check_which_present_made(presents, mixed)

    elif mixed > 499:
        mixed = mixed // 2
        if is_present_made(mixed):
            check_which_present_made(presents, mixed)

    else:
        check_which_present_made(presents, mixed)

if (presents['Gemstone'] >= 1 and presents['Porcelain Sculpture'] >= 1) \
        or (presents['Gold'] >= 1 and presents['Diamond Jewellery'] >= 1):
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')
if materials:
    print(f'Materials left: {", ".join([str(x) for x in materials])}')
if magics:
    print(f'Magic left: {", ".join([str(x) for x in magics])}')

for present, value in sorted(presents.items()):
    if value > 0:
        print(f'{present}: {value}')