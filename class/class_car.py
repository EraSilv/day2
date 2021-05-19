# # import datetime
# # now = datetime.datetime.now()

# oil_92 = 49.50
# oil_95 = 51.50

# class Car:
#     spend_100 = 12

#     def __init__(self, name , year, color , price, gasoline):
#         self.name = name
#         self.year = year
#         self.color = color
#         self.price = price
#         self.gasoline = gasoline
#     def get_gasoline(self,km):
#         r = (km / 100) * self.spend_100
#         print('absrobs for : ' , km , r)
#     def get_gasoline_price(self,km):
#         d = (km / 100) * self.spend_100*oil_92
#         s = (km / 100) * self.spend_100*oil_95
#         print('absrobing for 92 : ' , km , d)
#         print('absrobs for 95:' , km , s)
#     def get_name(self):
#         print('name:', self.name)
#     def get_year(self):
#         print('year:', self.year)
#     def get_color(self):
#         print('color:', self.color)
#     def get_price(self, current_year):
#         year_diff = current_year - self.year
#         # now = datetime.datetime.now()
#         # print('current date and time: ')
#         # print(now.strftime('%d-%m-%y'))
#         skidka = (self.price*0.05)*year_diff
#         print('price:', self.price - skidka)






# mycar = Car(
#     name = 'Lexus 570',
#     year = 2017,
#     color = 'white',
#     price = 25000,
#     gasoline = 5.7
    
    
#     )
# # print('car name:',mycar.name)
# # print('car year:',mycar.year)
# # print('car price:',mycar.price)
# # print('car color:',mycar.color)

# mycar.get_name()
# mycar.get_year()
# mycar.get_price(2021)
# mycar.get_color()
# mycar.get_gasoline(145)
# mycar.get_gasoline_price(145)


class Animal:
    def __init__(self,**kwargs):
        self.name = kwargs['name']
        self.type = kwargs['type']
        self.klass = kwargs['klass']
        



name = input('Input name of the animal: ')
lion = Animal(
    name = name,
    type = 'milky',
    klass = 'dangerous'


    
    )






