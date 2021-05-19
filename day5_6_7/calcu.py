# num1 = input(' give 1st number:')
# num2 = input(' give 2nd number:')

# num1 = int(num1)
# num2 = int(num2) 

# print(type(num1)) 
# print(type(num2))

# print('sum:', num1 + num2)
# print('sum:', num1 / num2)
# print('sum:', num1 - num2)
# print('sum:', num1 * num2)
# print('sum:', (num2 / num2) * num1 + num2)
# print('sum:', num1 % num2)


num1 = int(input('1st no.:'))
num2 = int(input('2nd no.:'))

symbol = input('whats the problem:')


print(num1 , symbol,num2, '=?')
# if symbol == '+': 
#     print(num1 + num2)
# if symbol == '-':
#     print(num1 - num2) 
# if symbol == '*':
#     print(num1 * num2)
if symbol == '/' and num1 != 0:
    print(num1 / num2)
    print(num1 / 0 )

# if symbol == '**':
#     print(num1 ** num2)


    
