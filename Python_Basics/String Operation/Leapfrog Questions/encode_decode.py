def logic(st):
    data = [char for char in st]

    def encode(st):

        new = []
        count = []
        ans = ''

        for letter in data:
            if letter not in new:
                new.append(letter)
        m = 0

        for l in new:
            num = st.count(new[m])
            count.append(num + 2)
            m += 1
        n = 0

        for i in count:
            ans = ans + str(count[n]) + (new[n])
            n += 1

        return ans

    def decode(t):
        decoded_str = ''
        c = 0
        for i in range(1, len(t)//2+1):
            decoded_str = decoded_str + (int(t[c])-2)*t[c+1]
            c += 2

        return decoded_str

    if data[0].isdigit():
        a = decode(data)

    else:
        a = encode(data)

    return a


text = input("Enter the string:")
output = logic(text)
print(output)
