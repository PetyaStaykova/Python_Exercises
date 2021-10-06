n_lines = int(input())
longest_intersection = set()

for _ in range(n_lines):
    first, second = input().split('-')
    start_1, end_1 = [int(x) for x in first.split(',')]
    start_2, end_2 = [int(x) for x in second.split(',')]
    first_range = set(range(start_1, end_1 + 1))
    second_range = set(range(start_2, end_2 + 1))
    current_intersection = first_range.intersection(second_range)
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection
longest_intersection_str = ', '.join([str(i) for i in longest_intersection])
print(f'Longest intersection is [{longest_intersection_str}] with length {len(longest_intersection)}')