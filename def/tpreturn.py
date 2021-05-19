# def square(x):
#     print(x**3)

# a = square(6)
# print(a)

# def square(x):
#     return x**3

# a = square(6)
# print(a)


# def square(x):
#     return x**3

# a = square(square(6))
# print(a)





#----chetnoe or net----------------

# def even(x):
#     if x%2==0:
#         return True
#     else:
#         return False

# for i in range(1,11):
#     print(i,even(i))

#-----------------OR-------------------

# def even(x):
#     if x%2==0:
#         return True
#     return False

# for i in range(1,11):
#     print(i,even(i))

#-----------------Factorial------------------

# def factorial(x):
#     pr=1
#     for i in range(2,x+1):
#         pr = pr*i
#     return pr

# for i in range (1,8):
#     print(i,factorial(i))
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# print('')

# def sochet (n,k):
#     return factorial(n) / (factorial(k) * factorial(n-k))

# print(sochet(5,3))
#------------------------------------------------------
def sqander(a,b):
    mas = []
    mas.append(a*b)
    mas.append(2*(a+b))
    return mas


    # return a*b,2*(a+b)


# print(sqander(3,6),type(sqander(3,6)))
print(sqander(2,6))



#----------------------------------------------------

