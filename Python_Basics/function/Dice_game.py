import random
import time

a1 = a2 = 0
player1 = input('Enter the name of first player::')
player2 = input('Enter the name of second player::')

for i in range(10):
    ch1 = input(f"{player1} Roll the dice by pressing 'r':: ")
    print(f'Rolling dice for {player1}:')
    time.sleep(1)
    if ch1.lower() == 'r':
        p1 = random.randint(1, 6)
        print(f'you got {p1}')
        a1 = a1 + p1
        if p1 == 6:
            print('Congrates you got a 6')
            print('Rolling the dice again')
            time.sleep(1)
            p1 = random.randint(1, 6)
            print(f'you got {p1}')
            a1 = a1 + p1

    ch2 = input(f"{player2} Roll the dice by pressing 'r':: ")
    print(f'Rolling dice for {player2}:')
    time.sleep(1)
    if ch1.lower() == 'r':
        p2 = random.randint(1, 6)
        print(f'you got {p2}')
        a2 = a2 + p2
        if p2 == 6:
            print('Congrates you got a 6')
            print('Rolling the dice again')
            time.sleep(1)
            p1 = random.randint(1, 6)
            print(f'you got {p2}')
            a1 = a1 + p1

    print(f'******************Round {i} finished********************')
    print()
    print()
    print(f'******************Round {i+1} Starts********************')
print()
print('Game Ends')
print(f'Score of {player1} is {a1}')
print(f'Score of {player2} is {a2}')

if a1 > a2:
    print(f"{player1} wins:")
if a1 < a2:
    print(f"{player2} wins")
else:
    print('Its a tie: Try playing again')