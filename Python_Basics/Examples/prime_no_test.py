def prime_test(num):
    if num == 1:
        print("Not Prime")
        exit()

    for i in range(2, num):
        if num % i == 0:
            print('Not Prime')
            exit()

    print('Prime')

number = prime_test(int(input("Enter the number to be tested::")))
