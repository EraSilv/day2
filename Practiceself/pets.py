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
# elif select_pet == 3:
#     petKey = input('kakuy Har: ')
#     if Python.get(petKey) != None:
#         print(petKey, Python[petKey])
#     else:
#         print('fuck off')
# else:
#     print('takoi mashiny netu')


#------------------------------------------------------------------------
#CAR

class car():
    name = '' 
    def setspeed(self, speed):
        print('Good going this fast: %d' % speed)

mycar = car()
mycar.setspeed(100)



class truck():
    name = '' 
    def setspeed(self, speed):
        print('Good going this fast: %d' % speed)


mytruck = truck()
mytruck.setspeed(90)





