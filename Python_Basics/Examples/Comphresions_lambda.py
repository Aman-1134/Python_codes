print(list(map(lambda x: x*x, range(1, 21))))
squares = [x*x for x in range(1, 11)]
print(squares)

print(list(filter(lambda x: x % 2 == 0, range(1, 21))))
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)
#alpha = [(c, i) for c in 'abcdefghij' for i in range(1, 11)]
#print(alpha)

z = zip([1, 2, 3], ['a', 'b', 'c'])
print(*z)

"""see this segment"""
nums = [1, 2, 4, 5, 3, 5, 7, 4, 6, 8, 9, 5, 4]
sqs = (num*num for num in nums)
print(next(sqs), next(sqs))
print(next(sqs))
print(next(sqs))


alpha = 'abcdefghi'
num = range(1, 10)
alphanum = {}

for c, i in zip(alpha, num):
    alphanum[c] = i
print(alphanum)

alphanum = {c: i for c, i in zip(alpha, num)}
print(alphanum)
