long_number = 123456782134567898543231415678765432134567
long_number_string = str(long_number)
print(long_number_string)
digit_count = dict()
#for digit in long_number_string:
 #   digit_count[digit] = 0
#for digit in long_number_string:
 #   digit_count[digit] += 1
#print(digit_count)

for digit in long_number_string:
    if not digit_count.get(digit):
        digit_count[digit] = 0

    digit_count[digit] += 1
print(digit_count)
