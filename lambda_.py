''' A lambda function is a small anonymous function.

 A lambda function can take any number of arguments, but can only have one expression.'''

'''The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:'''

# a= lambda x,y:(x+y,x-y)
# print(a(10,5))

# def fun(n):
#     return lambda a:a*n

# b=fun(5)
# print(b(5))

from recursion_ import fun

ans=fun()
print(ans)