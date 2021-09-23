data = input().split()
chars = {}

for word in data:
    for char in word:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1

for key, value in chars.items():
    print(f'{key} -> {value}')