def ids():
    lname = input('Enter the name of the person in order last name, first name and middle name:')
    fname = input()
    mname = input("If no middle name type 'N': ")

    if mname == 'N':
        full_name = fname + ' ' + lname

    else:
        full_name = fname + ' ' + mname + ' ' + lname

    return full_name


name = ids()
print(name)
