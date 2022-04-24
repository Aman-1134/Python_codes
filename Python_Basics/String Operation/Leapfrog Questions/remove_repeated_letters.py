"""
Problem::
If the letter in a sentence is non vowel and is repeated, remove the repeated letter.

Eg.
Sentence :: Hello my fellow peeps
Output :: Helo my felow peeps
"""


def logic(st):
    l = [char for char in st]
    vowels = ['a', 'e', 'i', 'o', 'u']
    update = []

    for i in range(0, len(l)-1):
        if i <= len(l)-2 and l[i] not in vowels and l[i] == l[i+1]:
            i += 1

        else:
            update += l[i]

    update += l[-1]

    t = "".join(update)
    print(t)


sen = input('Enter the sentence::')
logic(sen)

# Hello my fellow peeps
