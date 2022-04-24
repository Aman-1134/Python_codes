def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("Call method executed before {}".format(self.original_function.__name__))
        return self.original_function( *args, **kwargs)


#decorated_display = decorator_function(display)      <use this else use decorator>
#decorated_display()
@decorator_function
def display_info(name, age):
    print("Display info ran with positional arguments {}  {}".format(name, age))

@decorator_function      # =  display = decorator_function(display)
def display():
    print('display function ran')

#@decorator_class
#def display_info(name, age):
#    print("Display info ran with positional arguments {}  {}".format(name, age))


#@decorator_class
#def display():
#    print('display function ran')


display()
display_info('Aman', 21)


