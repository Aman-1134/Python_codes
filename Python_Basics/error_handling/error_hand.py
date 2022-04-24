try:
    # d = 1/0
    # new_var = non_extinent_var
    # n = [1,2,3]
    # print (n[5])
    # a = 9

    nu = 0
    de = 0
    if de == 0 and nu != 0:
        raise ZeroDivisionError('ZeroDenominator')
    else:
        q = nu/de
        print(q)

    if de == 0 and nu == 0:
        raise ArithmeticError('Zero numerator and denominator')
#e gives extra information ie what error has occured

except ZeroDivisionError as ze:
    print(ze)

except NameError as ne:
    print(ne)

except Exception as e:
    print(e)

else:
    print('No Errors')
finally:
    print('This executes no matter what')

print('a')