def form_word(string):      # takes the word list from  convert and forms a format to display
    # print('Number of digits is',len(string))
    if len(string) == 4:
        n4, n3, n2, n1 = string[0], string[1], string[2], string[3]
        hund = cmb_word(n2, n1)
        print('{} thousand {} hundred and {}'.format(n4, n3, hund))

    if len(string) == 5:
        n5, n4, n3, n2, n1 = string[0], string[1], string[2], string[3], string[4]
        hund = cmb_word(n2, n1)
        thou = cmb_word(n5, n4)
        print('{} thousand {} hundred and {}'.format(thou, n3, hund))

    if len(string) == 6:
        n6, n5, n4, n3, n2, n1 = string[0], string[1], string[2], string[3], string[4], string[5]
        hund = cmb_word(n2, n1)
        thou = cmb_word(n5, n4)
        print('{} lakh {} thousand {} hundred and {}'.format(n6, thou, n3, hund))

    if len(string) == 7:
        n7, n6, n5, n4, n3, n2, n1 = string[0], string[1], string[2], string[3], string[4], string[5], string[6]
        hund = cmb_word(n2, n1)
        thou = cmb_word(n5, n4)
        lakh = cmb_word(n7, n6)
        print('{} lakh {} thousand {} hundred and {}'.format(lakh, thou, n3, hund))

    if len(string) == 8:
        n8, n7, n6, n5, n4, n3, n2, n1 = string[0], string[1], string[2], string[3], string[4], string[5], string[6], string[7]
        hund = cmb_word(n2, n1)
        thou = cmb_word(n5, n4)
        lakh = cmb_word(n7, n6)
        print('{} crore {} lakh {} thousand {} hundred and {}'.format(n8, lakh, thou, n3, hund))
    if len(string) == 9:
        n9, n8, n7, n6, n5, n4, n3, n2, n1 = string[0], string[1], string[2], string[3], string[4], string[5], string[6], string[7], string[8]
        hund = cmb_word(n2, n1)
        thou = cmb_word(n5, n4)
        lakh = cmb_word(n7, n6)
        crore = cmb_word(n9, n8)
        print('{} crore {} lakh {} thousand {} hundred and {}'.format(crore, lakh, thou, n3, hund))

def cmb_word(n1, n2):       # takes argument from from_word function and gives their exact vaue
    if n1 == 'zero':
        return n2

    if n1 == 'one' and n2 == 'zero':
        return 'ten'

    if n1 == 'one' and n2 == 'one':
        return 'eleven'

    if n1 == 'one' and n2 == 'two':
        return 'twelve'

    if n1 == 'one' and n2 == 'three':
        return 'thirteen'

    if n1 == 'one' and n2 != 'one' and n2 != 'two' and n2 != 'three':
        return n2 + 'teen'

    if n1 =='two' and n2 =='zero':
        return 'twenty'

    if n1 == 'two' and n2 != 'zero':
        return 'twenty' + ' ' + n2

    if n1 == 'three' and n2 == 'zero':
        return 'thirty'

    if n1 == 'three' and n2 != 'zero':
        return 'thirty' + ' ' + n2

    if n1 == 'four' and n2 == 'zero':
        return 'forty'

    if n1 == 'four' and n2 != 'zero':
        return 'forty' + ' ' + n2

    if n1 == 'five' and n2 == 'zero':
        return 'fifty'

    if n1 == 'five' and n2 != 'zero':
        return 'fifty' + ' ' + n2

    if n1 == 'six' and n2 == 'zero':
        return 'sixty'

    if n1 == 'six' and n2 != 'zero':
        return 'sixty' + ' ' + n2

    if n1 == 'seven' and n2 == 'zero':
        return 'seventy'

    if n1 == 'seven' and n2 != 'zero':
        return 'seventy' + ' ' + n2

    if n1 == 'eight' and n2 == 'zero':
        return 'eighty'

    if n1 == 'eight' and n2 != 'zero':
        return 'eighty' + ' ' + n2

    if n1 == 'nine' and n2 == 'zero':
        return 'ninety'

    if n1 == 'nine' and n2 != 'zero':
        return 'ninety' + ' ' + n2


def form_list_of_word(num):       # takes list of number as arument and makes a list of their number words
    j = 0
    for i in num:
        if num[j] == 0:
            num[j] = 'zero'
        if num[j] == 1:
            num[j] = 'one'
        if num[j] == 2:
            num[j] = 'two'
        if num[j] == 3:
            num[j] = 'three'
        if num[j] == 4:
            num[j] = 'four'
        if num[j] == 5:
            num[j] = 'five'
        if num[j] == 6:
            num[j] = 'six'
        if num[j] == 7:
            num[j] = 'seven'
        if num[j] == 8:
            num[j] = 'eight'
        if num[j] == 9:
            num[j] = 'nine'

        j += 1

    return num


def convert(num):     # takes number as argument and makes a list of each number
    a = []
    j = 0
    y = str(num)
    x = len(y)
    if num % 10 ** x >10:      # number in range of pow(10,x)
        for i in range(1, x+1):
            ind = num // 10**(x-1)
            m = num % 10**(x-1)
            num = num % 10**(x-1)
            a.append(ind)
            j += 1
            x -= 1

    # print(a)
    new = form_list_of_word(a)
    # print(new)
    form_word(new)

# main function
n = int(input('Enter the no to convert to word:'))
if n == 0:
    print('It seems you typed zero, Type a number greater than 0:')
convert(n)
