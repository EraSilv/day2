
cars = {
    'MERS' : 2016,
    'Toyota': 2014,
    'kia' : 2008,
    'subary': 2006,
    'ferari': 2003

}
try:
    car_file = open('xar.txt', 'w')
    for key, value in cars.items():
        car_file.writelines(key + ',' +str(value) + '\n')



except FileNotFoundError:
    print('u dont have such a module or file!')

