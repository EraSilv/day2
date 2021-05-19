class animal():
    name = 'not named' #static

    def __init__(self):
        print('animal constructed')


class reptile(animal):
    hasScales = True #static

    def __init__(self):
        super(reptile,self).__init__() #must init the suoer
        print('reptile constructed')

class mammal(animal):
    hasHair = True #static

    def __init__(self):
        super(mammal,self).__init__() #must init the suoer
        self.hasBackBone = True
        print('mammal constructed')

class dragon(reptile,mammal):
    hasWings = True #static variable

    def __init__(self,age = 0):
        super(dragon,self).__init__() #must init the suoer
        self.age = age
        print('dragon constructed and is %d years old' % self.age)

    def __del__(self):
        print(self.__class__.__name__+'destroyed')

print('start')

mydragon1 = dragon(100)
mydragon1.name = 'San'
mydragon2 = dragon()

mydragon2.name = 'Sam'
# dragon.name = 'beka'


# print(mydragon1.name)

# print(mydragon2.name)


print('Hair = %s' % mydragon1.hasHair)
print('BackBone = %s' % mydragon1.hasBackBone)
print('%s is %d years old' % (mydragon1.name, mydragon1.age))

print('finished')

