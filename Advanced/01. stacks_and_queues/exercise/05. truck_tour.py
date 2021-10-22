from collections import deque
number_of_pumps = int(input())

pumps = deque()
for n in range(number_of_pumps):
    pump = [int(n) for n in input().split()]
    pumps.append(pump)
for i in range(len(pumps)):
    fuel = 0
    tour_completed = True
    for pump in pumps:
        gas = pump[0]
        distance = pump[1]
        fuel += gas
        if distance > fuel:
            tour_completed = False
            break
        fuel -= distance
    if tour_completed:
        print(i)
        break
    else:
        pumps.append(pumps.popleft())