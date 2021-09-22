year = int(input())

while True:
    year += 1
    year_as_str = str(year)
    if len(year_as_str) == len(set(year_as_str)):
        print(year)
        break