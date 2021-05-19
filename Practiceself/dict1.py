# a = ['moskva' , 'piter' , 'bishkek']
# a = [['moskva',495] , ['piter',812] , ['bishkek',312]]


# d = {
    # key:value,
#     'moskva' :  495,
#     'piter':  812, 
#     'bishkek':  312,
# #     1 :  'one',
#     2 :  'two', 
#     3 :  'three',


# }
# r = dict(moskva=495,piter=812,bishkek=312)
# # t = dict(a)
# q = dict.fromkeys(['a','b','c'],100)


# print(r)

#------------------------------------------------------------------------------------

# person = {}
# s = 'Ivanov Ivan Samara SGU 5 4 5 5 3 5'
# s = s.split()
# person['LastName'] = s[0]
# person['FirstName'] = s[1]
# person['city'] = s[2]
# person['University'] = s[3]
# person['marks'] = []
# for i in s[4:]:
#     person['marks'].append(int(i))
# print(s)
# print(person)


#--------------------------------------------------------------------------------------------------


# d = {
#     #key:value,  
#     1 :  'one',
#     2 :  'two', 
#     3 :  'three',


# }

# print(d)
# del d[1]
# print(d)
# print(len(d))
# print(1 in d, 5 in d, 7 not in d)
# if 5 in d:
#     print(d[5])
# else:
#     d[5] = 'five'
# print(d)
# print(d.keys())
# print(d.setdefault(6,'six'))

# print(d.items())
# for key,value in d.items():
#     print(key, value)
# for key in d:
#     print(key, d[key])

#-------------------------------------------------------------------------------
# ages = {'Bro':40 , 'Sis':22}
# for name,age in ages.items():
#     print('%s is %d years old' % (name,age))

#--------------------------------------------------------------------------------
# audi = {
#     'name' : 'audi a6',
#     'vol' : 4.0,
#     'color' : 'black',
#     'price' : 26000 

# }




# print('name:', audi['name'])
# print('vol:',audi['vol'])
# print('color:',audi['color'])
# print('price:',audi['price'],'$')

#--------------------------------------------------------------------------------------------
# cheetah = {
#     'name' : 'kitty',
#     'weight' : 80,
#     'color' : 'orange dotted',
#     'type' : 'milky',
#     'class' : 'predator',
#     'age':9

# }
# # print('name:',cheetah['name'])
# # print('weight:',cheetah['weight'])
# # print('color:',cheetah['color'])
# # print('type:',cheetah['type'])
# # print('class:',cheetah['class'])
# # print('age:',cheetah['age'])



# lion = {
#     'name' : 'Leo',
#     'weight' : 130,
#     'color' : 'orange dotted',
#     'type' : 'milky',
#     'class' : 'predator',
#     'age':7

# }
# # print('name:',lion['name'])
# # print('weight:',lion['weight'])
# # print('color:',lion['color'])
# # print('type:',lion['type'])
# # print('class:',lion['class'])
# # print('age:',lion['age'])



# Python = {
#     'name' : 'Sleak',
#     'weight' : 130,
#     'skin' : 'dark sexy',
#     'type' : 'milky',
#     'class' : 'predator',
#     'age': 'unknown'

# }
# # print('name:',Python['name'])
# # print('weight:',Python['weight'])
# # print('skin:',Python['skin'])
# # print('type:',Python['type'])
# # print('class:',Python['class'])
# # print('age:',Python['age'])


# print('Welcome to our Zoo!')
# print('available pets:')
# print('1:' , cheetah['class'])
# print('2:' , lion['class'])
# print('3:' , Python['class'])

# select_pet = int(input('PET:  '))
# if select_pet == 1:
#     print('Cheetah')
#     print('name:',cheetah['name'])
#     print('weight:',cheetah['weight'])
#     print('color:',cheetah['color'])
#     print('type:',cheetah['type'])
#     print('class:',cheetah['class'])
#     print('age:',cheetah['age'])
# if select_pet == 2:
#     print('LION  ')
#     print('name:',lion['name'])
#     print('weight:',lion['weight'])
#     print('color:',lion['color'])
#     print('type:',lion['type'])
#     print('class:',lion['class'])
#     print('age:',lion['age'])
# if select_pet == 3:
#     print('Python')
#     print('name:',Python['name'])
#     print('weight:',Python['weight'])
#     print('skin:',Python['skin'])
#     print('type:',Python['type'])
#     print('class:',Python['class'])
#     print('age:',Python['age'])

# else:
#     print('We have only 3 available classes')


# #---------------------------------------------------------------------------------------------------------------------------------
# cheetah = {
#     'name' : 'kitty',
#     'weight' : 80,
#     'color' : 'orange dotted',
#     'type' : 'milky',
#     'class' : 'predator',
#     'age':9

# }




# lion = {
#     'name' : 'Leo',
#     'weight' : 130,
#     'color' : 'orange dotted',
#     'type' : 'milky',
#     'class' : 'predator',
#     'age':7

# }

# Python = {
#     'name' : 'Sleak',
#     'weight' : 130,
#     'skin' : 'dark sexy',
#     'type' : 'milky',
#     'class' : 'predator',
#     'age': 'unknown'

# }

# print('Welcome to our Zoo!')
# print('available pets:')
# print('1:' , cheetah['class'])
# print('2:' , lion['class'])
# print('3:' , Python['class'])
# select_pet = int(input('which characteristic u want: '))

# if select_pet == 1:
#     petKey = input('kakuy Har: ')
#     if cheetah.get(petKey) != None:
#         print(petKey, cheetah[petKey])
#     else:
#         print('fuck off')
# elif select_pet == 2:
#     petKey = input('kakuy Har: ')
#     if lion.get(petKey) != None:
#         print(petKey, lion[petKey])
#     else:
#         print('fuck off')
# elif select_car == 3:
#     petKey = input('kakuy Har: ')
#     if Python.get(petKey) != None:
#         print(petKey, Python[petKey])
#     else:
#         print('fuck off')
# else:
#     print('takoi mashiny netu')



#-----------------------------------------------------------------------------------------------------------------


# Структура данных dict человека
# human = {
#     'fio': 'Торогулов Амантур',
#     'pol': "Мужчина",
#     'age': 13,
#     'ves': 31,
#     'rost': 162,
#     'address': 'Ош',
#     'birthday': '2 сентября 2007',
#     'school': 'itc_bootcamp',
#     'foot_razmer': 36,
#     'email':'human@mail.com',
#     'password': '2007a'
# }
# human['IQ'] = 110
# human['age'] = 26
# human.clear()
# print(human.keys())
# print(human['password'])
# print(human.values())

#------------------------------------------------------------------------------------------------------------------------------------------