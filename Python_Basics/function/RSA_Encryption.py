import random


# split message letters into characters
def split_message_to_char(word):
    return [char for char in word]


# choosing p and q (two prime numbers)
def prime_selector():
    lower = 1000
    upper = 10000
    x = []

    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break

            else:
                x.append(num)
    prime = random.choice(x)
    return prime


# calculating value of e
def calculate_e(n_e, z_e):
    lower_e = 3
    upper_e = 100
    x_e = []

    for num in range(lower_e, upper_e + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break

            else:
                x_e.append(num)

    for i in x_e:
        if i < n_e and z_e % i != 0:
            return i


# calculating d ( not necessary for only encryption )
def calculate_d(z_d):
    for i in range(1, 1000):
        if (z_d * i + 1) % e == 0:
            dd = (z_d * i + 1) / e
            return dd


# finally encrypt the message we receive
def encrypt_message(mes, n_encr, e_encr):
    en_m = []                            # variable to store encoded message
    en_number = []                       # to store number after mod operation
    for m in mes:
        en = ord(m) ** e_encr % n_encr   # ie m**e mod n
        en_number = en_number + [en]
        cypher_text = chr(en % 127)
        en_m = en_m + [cypher_text]

    str_encrypted = ''
    for m in en_m:
        str_encrypted = str_encrypted + m

    return str_encrypted


p = prime_selector()
q = prime_selector()
while p == q:
    q = prime_selector()

n = p * q
z = (p - 1) * (q - 1)

e = calculate_e(n, z)
d = calculate_d(z)

print(f'p = {p}, q = {q}, n = {n}, z = {z}')
print(f'e = {e}, d = {d}')

# message = 'I am Aman Ansari'
message = input('Enter Message to be Encrypted::')
print('Original Message is  = ', message)

splitted_message = split_message_to_char(message)

encrypted_message = encrypt_message(splitted_message, n, e)
print('Encrypted Message is = ', encrypted_message)
print(f'Public Key is ({n}, {e})')
