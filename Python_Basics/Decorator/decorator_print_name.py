import time

def capitalizer(func):
    def caller():              #nothing to receive as argument
        global end
        print(func().upper())
        print('*' * 10)
        end = time.time()

    return caller

@capitalizer
def take_name():
    global start
    name = input('Enter your name:: ')
    start = time.time()
    print('*' * 10)
    return name

take_name()                #nothing to send as argument

print("time taken = ", end - start)
