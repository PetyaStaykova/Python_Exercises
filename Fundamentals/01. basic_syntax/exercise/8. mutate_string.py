string_1 = input()
string_2 = input()
result_string = string_1

for i in range(len(string_1)):
    left_part = string_2[:i + 1]
    right_part = string_1[i + 1:]
    current_string = left_part + right_part
    if current_string == result_string:
        continue

    print(current_string)
    result_string = current_string