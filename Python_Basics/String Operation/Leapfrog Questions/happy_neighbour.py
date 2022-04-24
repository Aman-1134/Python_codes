# The function is expected to return an integer.
# The function accepts string as parameter.

def logic(my_input):
    # Write your code here and remove pass statement
    # You can create other functions and call from here
    # Don't print anything. Just return the intended output
    l = [char for char in my_input]
    uh = 0
    h = 0

    for num in range(0, len(l)):
        if num == 0:
            if l[num] == l[num + 1]:
                h += 1

        elif num >= 0 and num < len(l)-1:
            if l[num] == '0' and l[num-1] == '1' and l[num+1] != '1':
                h += 1

            elif l[num] == '0' and l[num - 1] != '1' and l[num + 1] == '1':
                h += 1

            elif l[num] == '1' and l[num-1] == '0' and l[num+1] != '0':
                h += 1

            elif l[num] == '1' and l[num - 1] != '0' and l[num + 1] == '0':
                h += 1

            elif l[num] == '0' and l[num - 1] == '0' and l[num + 1] == '0':
                h += 1

            elif l[num] == '1' and l[num - 1] == '1' and l[num + 1] == '1':
                h += 1
        elif num == len(l)-1:
            if l[num] == l[num-1]:
                h += 1

    return h

# Do not edit below

# Get the input
my_input = input()

# Print output returned from the logic function
print(logic(my_input))
