#def print_name(fname, lname, age):
#def print_name(*args):
   # print('my name is {} {} and I am {} years old'.format(*args[0],*args[1],args[2]))
  #  print(f" my name is {args[0]} {args[1]} and i am {args[2] } years old")
    #print(fname, lname, age)
#print_name('Aman','Ansari',21)

def factorial(num):
    if num == 1:
        return num
    else:
         return num*factorial(num-1)
#i=1
#def fact(num):
 #   if i == num
  #      return x
   # else:
    #    x = i*fact(i+1)

a=factorial(10)
print(a)