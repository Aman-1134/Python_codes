import logging

def add(x,y):
    return x+y

logging.basicConfig(filename='Files/test.log', format='%(asctime)s:%(levelname)s:%(message)s',
                    level=logging.DEBUG)


num_1 = 5
num_2 = 7
add_result = add(num_1, num_2)
print(f"Add : {num_1} + {num_2} = {add_result}")
logging.debug(f"Add {num_1} + {num_2} = {add_result}")
