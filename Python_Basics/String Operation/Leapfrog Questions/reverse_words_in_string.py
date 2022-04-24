def reverseWords(s):
    m = 0
    l = s.split()
    print(l)
    m = len(l)-1
    z = []
    for i in range(0, len(l)):
        z.append(l[m])
        m = m-1

    ans = " ".join(z)
    return ans

answer = reverseWords("i am aman ansari")
print(answer)


