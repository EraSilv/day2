#---------args, dynamics get parameters!-----------------

# def simple (a ,b,*args):
#     print(a,b,args[0],args[1],args[2],args[3],args[4],args[5])

# simple(10,20,30,40,50,60,70,80)


# def simple (*args):
#     sum = 0
#     for i in args:
#         sum = sum + i 

#     print(sum)



# simple(30,40,50,8,56,13,10**2)



#-------------KWARGS-------------------------
def simple (**kwargs):
    print(kwargs['name'])
    print(kwargs['model'])
    print(kwargs['year'])
    print(kwargs['price'])

simple(
    name = 'camry', 
    model = '3.5',
    year = '2012',
    price = '27000$'
    )

def mypc(**kwargs):
    print(kwargs['processor'])
    print(kwargs['cd'])
    print(kwargs['video'])
    print(kwargs['ram'])
    print(kwargs['model'])
    print(kwargs['price'])

print('')

mypc(
    processor = 'AMD Ryzen 5',
    cd = '1024 gb',
    video = '1080HD',
    ram = '1024 gb',
    model = 'ACER MFC',
    price = '12000$'

)

