def is_length_valid(password):
    if 6 <= len(password) <= 10:
        return True
    return False


def consists_only_of_letters_and_numbers(password):
    return password.isalnum()


def has_at_least_two_digits(password):
    digits_count = 0
    for symbol in password:
        if symbol.isnumeric():
            digits_count += 1
    if digits_count >= 2:
        return True
    else:
        return False


def is_password_valid(password):
    is_valid = True
    if not is_length_valid(password):
        print('Password must be between 6 and 10 characters')
        is_valid = False
    if not consists_only_of_letters_and_numbers(password):
        print('Password must consist only of letters and digits')
        is_valid = False
    if not has_at_least_two_digits(password):
        print('Password must have at least 2 digits')
        is_valid = False
    if is_valid:
        print('Password is valid')


password_from_input = input()
is_password_valid(password_from_input)

