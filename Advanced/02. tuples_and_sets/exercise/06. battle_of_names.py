n_lines = int(input())

even_set = set()
odd_set = set()

for line in range(1, n_lines + 1):
    name = input()
    calculated_name = sum([ord(ch) for ch in name]) // line

    if calculated_name % 2 == 0:
        even_set.add(calculated_name)
    else:
        odd_set.add(calculated_name)

result = set()
even_set_sum = sum(even_set)
odd_set_sum = sum(odd_set)

if even_set_sum == odd_set_sum:
    result = odd_set.union(even_set)
elif even_set_sum > odd_set_sum:
    result = odd_set.symmetric_difference(even_set)
else:
    result = odd_set.difference(even_set)
print(', '.join([str(i) for i in result]))