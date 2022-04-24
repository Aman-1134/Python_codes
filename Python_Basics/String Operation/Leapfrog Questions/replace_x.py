"""
Question
Replace all x by 'cks' unless;
1. First letter of word is 'x'. Here replace x by z.
2. The letter is only 'x'. Replace x by 'ecks'.
"""

""" Run All these Statements
1. x Oxen is running x with xylophone x
2. x Oxen is running x with xylophone x.
3. Oxen is running x with xylophone x
4. xen oxen is running x with xylophone x.
"""


text = "xen oxen is running x with xylophone x."
update = []


def logic(st):
    l = [char for char in st]

    for i in range(0, len(l)):
        # first or last letter is x and no full stop present
        if i == 0 and l[i] == 'x' and l[1] == ' ' or i == len(l)-1 and l[i] == 'x' and l[i-1] == ' ':
            update.append('ecks')

        # last letter is x and has a full stop
        elif i == len(l)-2 and l[i+1] == '.' and l[i] == 'x' and l[i-1] == ' ':
            update.append('ecks')

        # any middle letter is x.
        elif l[i] == 'x' and l[i-1] == ' ' and l[i+1] == ' ':
            update.append('ecks')

        # if 1st letter of word is x
        elif l[i] == 'x' and l[i+1] != ' ' and l[i-1] == ' ' or i == 0 and l[i] == 'x' and l[i+1] != ' ':
            update.append('z')

        # for all remaining x'es
        elif l[i] == 'x':
            update.append('cks')

        else:
            update.append(l[i])


logic(text)
t = "".join(update)
# print(text)
print(t)

