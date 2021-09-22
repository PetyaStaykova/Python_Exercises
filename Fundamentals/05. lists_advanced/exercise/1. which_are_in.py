first_list = input().split(', ')
second_list = input().split(', ')

list_of_found_elements = [word for word in first_list if any(word in x_word for x_word in second_list)]
print(list_of_found_elements)