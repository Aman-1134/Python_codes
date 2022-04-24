capitala = ord('A')
capitalz = ord('Z')
smalla = ord('a')
smallz = ord('z')   # Not required in program
for i in range(capitala, capitalz+1):  # can use capitala + 26 instead of capitalz+1
    print(chr(capitala), chr(smalla), end='    ')
    capitala = capitala+1
    smalla += 1
