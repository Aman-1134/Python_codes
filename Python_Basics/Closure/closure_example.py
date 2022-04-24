def outer_fun(message):

    def inner_fun(person):
        return f"{message}, {person}"
    return inner_fun


print(outer_fun('bye')('Amit kale'))
hi = outer_fun('hi')
bye = outer_fun('bye')

print(hi('Aman'))
print(bye('Darsan'))


def add(x, y):
    return x + y


def printer(func):
    def print_info(x, y):
        print(f"ADDITION of {x}, {y}")
        print(f"RESULT: {func(x,y)}")
    return print_info


add_printer = printer(add)

print(add(1, 2))
add_printer(1, 2)
