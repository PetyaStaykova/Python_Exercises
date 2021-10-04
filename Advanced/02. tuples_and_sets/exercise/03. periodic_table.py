n_lines = int(input())

unique_elements = set()

for _ in range(n_lines):
    chemical_compound = [unique_elements.add(x) for x in input().split()]

[print(x) for x in unique_elements]