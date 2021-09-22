def is_palindrome(list_of_int):
    it_is_palindrome = True
    str_from_the_list = list_of_int.split(', ')
    for i in str_from_the_list:
        if i == i[::-1]:
            print("True")

        else:
            it_is_palindrome = False
            print("False")
    return it_is_palindrome


input_info = input()
result = is_palindrome(input_info)