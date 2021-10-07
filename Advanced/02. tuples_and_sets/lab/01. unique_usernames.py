n_lines = int(input())

unique_usernames = set()

for _ in range(n_lines):
    username = input()
    unique_usernames.add(username)
[print(username) for username in unique_usernames]