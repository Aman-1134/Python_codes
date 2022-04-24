text = """
sorry this page cant be found
"""
print(text.split())
words = text.split()
print(len(words))

for ctr, word in enumerate(words):
    if word.lower() == 'sorry':
        words[ctr] = 'haha'
    ctr += 1
print(words)
new_text = ''
for word in words:
    new_text = new_text + ' ' + word
print(new_text.strip())

#
# text = "Sorry the page cant be found."
# new = []
# ctr = 0
# def changer(string_n):
#     st = string_n.split()
#     for word in st:
#         if word.lower() == "sorry":
#             word = "haha"
#             new.append(word)
#         else:
#             new.append(word)
#
# print(text)
# changer(text)
# t = " ".join(new)
# print(new)
# print(t.capitalize())
