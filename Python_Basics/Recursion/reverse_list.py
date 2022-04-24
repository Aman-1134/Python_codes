def reverse(num,i,j):
    print(num)
    if i >= len(num) // 2:
        return num
    else:
        x = num[i]
        num[i] = num[j]
        num[j] = x
        i +=1
        j -= 1
        return reverse(num,i,j)
lon = [1,2,3,4,5,6,7,8,9,10]
a = reverse(lon,0,-1)
print(a)
