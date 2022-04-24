import time
Available_Balance = 10000


def delay_info():
    print('Processing Transaction........')
    time.sleep(1)
    print('Please Wait...................')
    time.sleep(2)


def transaction_success():
    print('Transaction Completed.........')
    time.sleep(1)


def menu(amount):
    time.sleep(2)
    print()
    print('1.Balance Inquiry')
    print('2.Cash Withdrawal')
    print('3.Cash Deposit')
    print('4.Fund Transfer')
    print('5.Bill Payment')
    print('9.Exit')

    print()

    choice = int(input('Choose Your Option::'))

    if choice == 1:
        balance_inquiry(amount)

    elif choice == 2:
        withdraw(amount)

    elif choice == 3:
        deposit(amount)

    elif choice == 4:
        fund_transfer(amount)

    elif choice == 5:
        bill_payment(amount)

    elif choice == 9:
        exit()

    else:
        print('Please enter a valid option')
        time.sleep(2)
        menu(amount)


def insufficient_balance():
    print('Insufficient Balance. Please check your balance first.')


def balance_inquiry(amount):
    time.sleep(1)
    print(f'Your Balance is = {amount}')
    time.sleep(2)
    menu(amount)


def withdraw(amount):
    time.sleep(2)
    withdraw_amount = int(input('Enter amount to be withdrawn::'))
    delay_info()

    if withdraw_amount > amount:
        insufficient_balance()
    else:
        amount = amount - withdraw_amount
        transaction_success()

    menu(amount)


def deposit(amount):
    time.sleep(2)
    deposit_amount = int(input('Enter Amount to be deposited::'))
    delay_info()

    amount = amount + deposit_amount
    transaction_success()

    time.sleep(2)
    menu(amount)


def fund_transfer(amount):
    time.sleep(1)
    account_no = input('Enter the Account Number::')
    if len(account_no) != 10:
        print('Enter a valid 10 digit Account Number')
        fund_transfer(amount)

    time.sleep(0.5)
    name = input('Enter name of Account Holder::')
    time.sleep(0.5)
    transfer_amount = int(input('Enter the amount to be transferred::'))
    delay_info()

    if len(name.split()) == 1:
        l_name = name
    if len(name.split()) == 2:
        f_name, l_name = name.split(' ')
    if len(name.split()) == 3:
        f_name, m_name, l_name = name.split(' ')

    account_no = '*******' + account_no[7] + account_no[8] + account_no[9]

    if transfer_amount > amount:
        insufficient_balance()

    else:
        amount = amount - transfer_amount
        transaction_success()
        print(f'Fund Rs {transfer_amount} successfully transferred to Mr {l_name} with account number {account_no}')
        time.sleep(1)

    menu(amount)


def bill_payment(amount):
    time.sleep(1)
    print('a.Electricity')
    print('b.Water')
    print('c.WIFI')
    print()

    purpose = input('Enter what bill is to be paid::')

    if purpose.lower() == 'a':
        purpose = 'Electricity'
    elif purpose.lower() == 'b':
        purpose = 'Water'
    elif purpose.lower() == 'c':
        purpose = 'Wifi'

    bill = int(input('Enter amount to be paid::'))
    delay_info()

    if bill > amount:
        insufficient_balance()
    else:
        amount = amount - bill
        transaction_success()
        time.sleep(1)
        print(f'Bill for {purpose} amount Rs {bill} paid')

    menu(amount)


def print_slip():
    pass


menu(Available_Balance)
