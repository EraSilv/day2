class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def printmy(self):
        print("I am ", self.__name, "I am", self.__age)


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printmy(self):
        print("I am ", self.name, "I am", self.age)

adam = Person2("Adam", 25)
adam.printmy()
print(adam.name)



adam = Person("Adam", 25)
# adam._Person__name = "men"
print(adam._Person__name)