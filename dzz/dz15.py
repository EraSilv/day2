# calculation_to_seconds = 24 * 60 * 60



# # print(calculation_to_seconds)
# name_of_unit = "seconds"


# n = int(input('enter amount of days,please: '))

# if n != 0:

#     print(n,'days are: ', n * calculation_to_seconds , name_of_unit)
# else:
#     print('are u fool? hows zeros?')

# print(n,'days are: ', n * calculation_to_seconds , name_of_unit)


# fruits = {
#    'алма':'🍎',
#    'дарбыз':'🍉',
#    'дыня':'🍈',
#    'помидор': '🍅',
#    'кулпунай': '🍓',
#    'банан': '🍌'
# }





# a = 0
# while a < 3:
#     s = input('enter: ')

#     if s in fruits:
#         print(fruits[s])
#         a = a + 1

#     else:
#         print('ENTER CORRECTLY FRUIT NAME!')




# def season(x):
#     if x >= 3 or x < 6:
#         print('SPRINg')
#     elif x >=1 or x <4:
#         print('Winter')
#     elif x >= 6 or x < 10:
#         print('Summer')
#     elif x >=9 or x <13:
#         print('fall')

# x = (int(input('enter smth: ')))

# season(x)




money = int(input('Money: '))
year = int(input('until: '))

def deposite(money,year):

    s = (money * 0.15)*year
    a = money + s
    print('for {0} years money were increased for {1}'.format(year,a))
deposite(money,year)







   