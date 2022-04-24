# give a string. checks if it is a palindrome. if not palindrome, program converts it to palindrome.
def ReverseStr(str):
    reverseStr = ""
    for i in str:
        reverseStr = i + reverseStr

    return reverseStr


str = input("ENTER YOUR STRING:: ")
pallindromeStr = ""
initialCheck = ReverseStr(str)
if str == initialCheck:
    print("FINAL PALLINDROME:: ", str)
else:
    for i in range(len(str)):
        pallindromeStr = pallindromeStr + str[len(str)-(i+1)]
        cutchar = str[:len(str)-(i+1)]    # i+1 is bcz in the loop i starts with 0 and thus in the beginning str index will goes out of scope of str
        tempstr = ReverseStr(cutchar)
        if cutchar == tempstr:
            finalpal = pallindromeStr + str
            print("FINAL PALLINDROME:: ", finalpal)
            break






# def pal(str):
#     ret_str = ""
#     for i in str:
#         ret_str = i + ret_str
#
#     return ret_str
#
# def construct_pal(str):
#     for i in str:
#         c_str = str
#         c_str = c_str + i
#         ret_str = pal(c_str)
#         if c_str == ret_str:
#             print(f'Constructed palindrome is {c_str}')
#             break
#
#         else:
#             construct_pal(c_str)
#
# str = input('Enter a string to check for palindrome::')
# ret_str = pal(str)
#
# if ret_str == str:
#     print('Palindrome')
#
# else:
#     print('Not a palindrome so constructing it.................')
#     construct_pal(str)
