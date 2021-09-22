n_lines = int(input())
capacity = 255
litters_in_tank = 0

for times_to_pour in range(1, n_lines + 1):
    litters_of_water = int(input())
    litters_in_tank += litters_of_water
    if litters_in_tank > capacity:
        print('Insufficient capacity!')
        litters_in_tank -= litters_of_water
    else:
        continue

print(litters_in_tank)