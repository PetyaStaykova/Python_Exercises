n = int(input())
parking = set()

for _ in range(n):
    command, car = input().split(', ')
    if command == 'IN':
        parking.add(car)
    else:
        if car in parking:
            parking.remove(car)
if parking:
    [print(car) for car in parking]
else:
    print('Parking Lot is Empty')