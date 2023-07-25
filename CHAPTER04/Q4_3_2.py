def func_square(*args):
    return [n * n for n in args]


numbers = [1, 2, 3, 4]
print(func_square(*numbers))
