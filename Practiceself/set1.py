# a = [1,2,3,1,2,3,4,1,2,3]
# b = {'hi', ' lol', 'bitch', 'he', 'ha', 'ho','hi' , 'ho', 'hi'}
# c = set('abrakaadbra')
# d = set([1,2,3,4,56,4,2,3,1])
# e = set(range(5))
# f = {}
# a = list(set(a))
# print(c)

#-----------------------------------------------------------------------------
# a = {1,2,2,34,4,3,54,4}
# a.add(9)
# # a.update([5,6,7,5])
# a.discard(4)
# print(a)

# b = {3,4,5,6,7}
# c = {10,11,12}
# print(a.intersection(b))
# a.intersection_update(b)
# print(a, b)
# print(4 in a,7 in a)

# print(a.union(b))

# a = a.union(b)
# a |= b
# print(b ^ a)


#------------------------------------------------------------------------
# text = input()
# a = set()
# while text != '':
#     slova = text.split()
#     a.update(slova)
#     print(a)
#     text = input()
# print(len(a))
#-----------------------------------------------------------------------------------

# emails = [
#     'era4565@gmail.com',
#     'zak@gmail.com',
#     'nur4565@gmail.com',
#     'ama4565@gmail.com',
#     'beka4565@gmail.com',
#     'ama4565@gmail.com'
    
# ]
# emails = set(emails)
# for email in emails:
#     print('FOR MAIL', email , 'Sent a message')

# emails.add('SSAS@gmAIL.com')
# emails.add('hkfajhdsk@gmAIL.com')


# print(emails)

#------------------------------------------------------------------------------------------------------------
# prod = {
#     'Samsa',
#     'kymyz',
#     'kurut',
#     'lagman',
#     'plov',
#     'soup'
# }

# # meal = ''.lower()
# # for meal in range(4): 
# #     meal = input('buy:')
# #     prod.add(meal.lower())
# lol = { 'lol' , 'kuurdak' , 'samsa', 'kurut','lagman'}
# # prod.update(lol)
# # print(prod)
# dif = prod.difference(lol)
# # print(prod.difference(lol))
# print(dif)
#------------------------------------------------------------------------------------------------------------------------

# name = {
#     'era',
#     'beka',
#     'zaka',
#     'aika',
#     'iska',
#     'zarlyk',
#     'emir',
#     'nur',
#     'aman'
# }


# lot = int(input('Enter amount of places:'))

# p1 = ''
# p2 = ''
# p3 = ''

# # print(name.pop())
# # p1 = print('1 place:' , name.pop())
# # p2 = print('2 place:' , name.pop())
# # p3 = print('3 place:', name.pop())
# for i  in range(lot):
#     print(i, '1 place......:', name.pop())
#     print(i, '2 place......:', name.pop())
#     print(i, '3 place......:', name.pop())
#----------------------------------------------DZZZZZZZZZZZZZ-------------------------------------------


# name = {
#     'era',
#     'beka',
#     'zaka',
#     'aika',
#     'iska',
#     'zarlyk',
#     'emir',
#     'nur',
#     'aman'
# }

# name.add('samsa')
# print(name)
# print(name.pop())
# print(name)
#--------------------------------------------------------------------------------------------------------------------------------------




# meal = {
#     'Plov': 140,
#     'Pizza': 350,
#     'pirozhok': 354,
#     'spicy-meat': 666,
#     'logman': 110,
#     'Faiza':125,
#     'meat':99,
#     'tibbon':55,
#     'borsh' : 70
# }

# meal['besh_barmak'] = 130
# meal['logman'] = 135
# del meal['borsh']
# meal['drinks'] = [
#     'Coca-Cola',
#     'Sprite', 
#     'Fanta']
# print(meal)
#----------------------------------------------------------

# info = {
#     '1name' : 'Roma',
#     'lastname' : 'Volk',
#     'gender' : 'male',
#     'age':25,
#     'personal_password': 1245
# }





# a = 0
# while a <= 2:
#     # do rest of the stuffs
    
#     s = input('First NAme: ').title()
#     if s == 'Roma':
#         print('Next------------->:')
#         pin = int(input('Password: '))    
#         if pin == 1245:
#             print('Welcome! ')
#         else:
#             print('ERROR PIN!')

#     else:
#         print('ERROR NAME!')
#     a += 1
#--------------------------------------------------------------------------------------------
# sas = [
#     {
#         'Roma' : 'Boss',
#         'age' : 26
#     },
#     {
#         'Vlad' : 'Secretary',
#         'age' : 26
#     },
#     {
#         'Kar' : 'Manager',
#         'age' : 19
#     },
#     {
#         'Eve' : 'HR',
#         'age' : 20
#     },
#     {
#         'Damon' : 'millionaire',
#         'age' : 25
#     }
# ]

# print('Welcome! Roma is our',sas[0]['Roma'],'. ' 'He is ',sas[0]['age'])
# print('Welcome! Vlad is our',sas[1]['Vlad'],'. ' 'He is ',sas[1]['age'])
# print('Welcome! Kar is our',sas[2]['Kar'],'. ' 'She is ',sas[2]['age'])
# print('Welcome! Eve is our',sas[3]['Eve'],'. ' 'She is ',sas[3]['age'])
# print('Welcome! Damon is our',sas[4]['Damon'],'. ' 'He is ',sas[4]['age'])


# suitcase = [

# ]
# suitcase = ['money' , 'gun' , 'money','money','money']
# suitcase.remove('money')
# print(suitcase)