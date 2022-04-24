def sqs(nums):
    for num in nums:
        yield(num*num)

sq = sqs([1,2,3,4,5,6,7,8])

print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))

print(type(sq))

print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))


