from collections import deque

males = [int(x) for x in input().split() if int(x) > 0]
females = deque([int(x) for x in input().split() if int(x) > 0])
matches = 0

while males and females:
    female = females.popleft()
    male = males.pop()
    if female % 25 == 0:
        females.popleft()
        males.append(male)
        continue
    if male % 25 == 0:
        males.pop()
        females.appendleft(female)
        continue

    if female == male:
        matches += 1
    else:
        if male > 2:
            males.append(male - 2)

print(f'Matches: {matches}')

if males:
    reversed_males = []
    for male in range(len(males)):
        reversed_males.append(males.pop())
    print(f"Males left: {', '.join([str(x) for x in reversed_males])}")
else:
    print('Males left: none')

if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print('Females left: none')