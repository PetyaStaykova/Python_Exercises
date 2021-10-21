def numbers_searching(*args):
    missing_value = None
    start_range = min(args)
    end_range = max(args)
    unique_numbers = set(args)

    for i in range(start_range, end_range + 1):
        if i not in unique_numbers:
            missing_value = i
            break
    repeating_numbers = set([x for x in args if args.count(x) > 1])
    return [missing_value, sorted(repeating_numbers)]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))