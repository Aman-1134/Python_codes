def convert_to_digits(n, suffix):
    if n == 0:
        return ZERO
    if n > 19:
        return string_above_19[n//10] + string_to_19[n % 10] + suffix
    else:
        return string_to_19[n] + suffix


def convert_to_words(n):
     results = convert_to_digits((n//100000000000) % 100, " Kharab, ")
     results += convert_to_digits((n//1000000000) % 100, " Arab, ")
     results += convert_to_digits((n//10000000) % 100, " Crore, ")
     results += convert_to_digits((n//100000) % 100, " Lakh, ")
     results += convert_to_digits((n//1000) % 100, " Thousand, ")
     results += convert_to_digits((n // 100) % 10, " Hundred, ")
     if n > 100 and n % 100:
         results += "and "

     results += convert_to_digits((n % 100), "")

     print(results)


ZERO = ""
string_to_19 = [ZERO, "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ",
                "Eight ", "Nine ", "Ten ", "Eleven ", "Thirteen ", "Fourteen ",
                "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "]

string_above_19 = [ZERO, ZERO, "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ",
                   "Seventy ", "Eighty ", "Ninety "]

number = int(input("Enter the number:: "))
convert_to_words(number)
