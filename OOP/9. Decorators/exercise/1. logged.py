def logged(func):
    def wrapper(*args):
        result = f'you called {func.__name__}{args}'
        func_result = func(*args)
        return f'{result}\nit returned {func_result}'

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))