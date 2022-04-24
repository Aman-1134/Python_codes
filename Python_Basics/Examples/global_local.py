x = 'global'

def outer():
    x = 'outer'
    def inner():
        global x
        x = 'inner'
        print(x)
    print(x)
    inner()
    print(x)
print(x)
outer()
print(x)



