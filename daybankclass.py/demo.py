import random

a = [
    'Lexus 570']






class Car:
    print('Car number one is constructed:' )
    
    def __init__(self):
        self.name = ' '
        self.year = ' '
    
    

car = Car()



name = input('Name of the car u r looking for: ').title()
price = random.randint(20000 , 60000)
category = random.randint(1 , 100)
# phone = random.randint((9))

if name == 'Lexus' or name == 'Lexus 570':
    car.name = name
    print('CAr:',a[0],'\n','Price:',price,'\n','Found:',category)


# Toyota.name = 'Camry 3.5',
# Toyota.year = '2018'

# Mercedes.name = 'Mercedes-Benz S-class',
# Mercedes.year = '2006'



# print('Car number one is : ' , car.name)
# print('Year: ',car.year)
# print('')

# print('Car number two is constructed: ')
# print('Car number two is : ' , Toyota.name)
# print('Year: ',Toyota.year)

# print('')

# print('Car number three is constructed: ')
# print('Car number three is: ', Mercedes.name)
# print('Year: ',Mercedes.year)






