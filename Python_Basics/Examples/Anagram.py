def anagram(text_a, text_b):
    if sorted(text_a) == sorted(text_b):
        print('Anagram')
    else:
        print('Not Anagram')


anagram('apple', 'pale')


# def anagram(txta, txtb):
#     sta = 0
#     stb = 0
#     if len(txta) == len(txtb) and set(txta) == set(txtb):
#         x = list(txta)
#         y = list(txtb)
#         for i in txta:
#             sta = sta + ord(i)
#
#         for j in txtb:
#             stb = stb + ord(j)
#
#         if sta == stb:
#             print('Anagram')
#         else:
#             print('Not Anagram')
#
#     else:
#         print('Not Anagram')
#     print("Sum of orders of first word =", sta)
#     print("Sum of orders of second word =", stb)
# anagram('goodbye','dogeoby')
