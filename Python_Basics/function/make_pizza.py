"""abc"""


def make_pizza(*toppings):
    """Make a pizza with supplied toppings """
    print("Making a pizza with the following toppings")
    for topping in toppings:
        print(f"-{topping}")


def make_pizza_ofsize(size, *toppings):
    print(f"Making a {size} inch pizza with following toppings:")
    for topping in toppings:
        print(f"-{topping}")


print(__name__)
make_pizza('Mushroom', 'chicken', 'tomato')
print()
print()
make_pizza_ofsize(14, 'Mushroom', 'chicken', 'tomato', 'Margerita')
