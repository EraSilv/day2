myaccount = [
    {
        "name": 'Demir Bank',
        "balance": 320000000.95,
        "currency" : '€',
        "PIN": 1526
    },
    {
        "name": 'Optima Bank',
        "balance": 20000000 ,
        "currency" : '€',
        "PIN": 4563

    },
    {
        "name": 'KICB',
        "balance": 15000000.23 ,
        "currency" : '€',
        "PIN": 7412
    },
    {
        "name": 'Dos-Credo Bank',
        "balance": 460000.17 ,
        "currency" : '€',
        "PIN": 1414
    },
]

#kurs valuta
cripto = {
    'EUR':101.35,
    'USD': 84.70,
    'RUB': 1.14

}



# for index in range(4):
#     print(index +1,':',banks[index]['name'])

# select_bank = int(input('choose bank: '))
# # print('Balance:')
# # print(banks[select_bank]['balance'], banks[select_bank]['currency'])
# if select_bank < 5 and select_bank >= 1:
#     print(banks[select_bank - 1]['balance'],banks[select_bank - 1]['currency'])

# else:
#     print('Dont ruin my program! Go away!!!')
print('MYaccount: ')
for index in range(4):
    print(index + 1, ':',myaccount[index]['name'])


aindex = int(input('Choose account: '))

if aindex < 5 and aindex >= 1:
    rindex = aindex - 1
    print('Bank', myaccount[aindex - 1]['name'])
    PIN = int(input('Enter Pin: '))
    # if PIN == 1526:
    #     int(input('How much money do u want :  '))

    # else:
    #     print('Error PIN! ')
    if PIN == myaccount[rindex]['PIN']:
        print('Welcome to', myaccount[rindex]['name'])
        s =int(input('How much do u wanna:  '))
        if s != 0:
            print('DownLoad.......')


        else:
            print('Please enter amount of money!')



    else:
        print('Error PIN!! ')
        

else:
    print('NO such an account!!  ')




