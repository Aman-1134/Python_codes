text = 'A technology company'


def logic(st):
    st_l = st.lower()

    c_a = st_l.count('a')
    c_e = st_l.count('e')
    c_i = st_l.count('i')
    c_o = st_l.count('o')
    c_u = st_l.count('u')

    count = [c_a, c_e, c_i, c_o, c_u]
    vowels = ['a', 'e', 'i', 'o', 'u']

    if c_a == 0 and c_e == 0 and c_i == 0 and c_o == 0 and c_u == 0:
        print("No vowels are present")
        exit()

    ans = ''
    m = 0

    for c in count:
        if c != 0:
            ans = ans + str(c) + vowels[m]
        m += 1

    return ans


output = logic(text)
print(output)
