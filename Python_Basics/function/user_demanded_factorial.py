s = 'y'

while s.lower() == 'y':
    fact = 1
    num = int(input('Enter the number :: '))
    while num != 1:
        fact = fact * num
        num -= 1

    print(fact)

    print('Do you want to continue::')
    print('Type Y for yes::')
    s = input()