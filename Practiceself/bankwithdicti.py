

banks = [
    {
        "name": 'Demir Bank',
        "address": 'ул. Курманжан-Датка 180а',
        "balance": 320000000.95,
        "currency" : '€'
    },
    {
        "name": 'Optima Bank',
        "address": 'ул. Гапар Айтиев 6/1',
        "balance": 20000000 ,
        "currency" : '€'
    },
    {
        "name": 'KICB',
        "address": 'ул. Курманжан-Датка 202а',
        "balance": 15000000.23 ,
        "currency" : '€'
    },
    {
        "name": 'Dos-Credo Bank',
        "address": 'ул. Ленина 314а',
        "balance": 460000.17 ,
        "currency" : '€'
    },
]
# a = int(input('enter index:'))
# print(banks[a]['name'],banks[0]['address'],bank['currency'])
# print(banks[0]['name'], banks[0]['address'],bank['currency'])
# print(banks[1]['name'], banks[1]['address'],bank['currency'])
# print(banks[2]['name'], banks[2]['address'],bank['currency'])
# print(banks[3]['name'], banks[3]['address'],bank['currency'])

#-----------------------------------------------WORK_---------------------------------------
# for bank in banks:
#     print(bank['name'],bank['address'],':', bank['balance'],bank['currency'])

# s = int(input('check balance: '))
# if s == 0:
#     print(bank[0]['balance'],bank['currency'])
# elif s == 1:
#     print(bank[1]['balance'],bank['currency'])
# elif s == 2:
#     print(bank[2]['balance'],bank['currency'])
# elif s == 3:
#     print(bank[3]['balance'],bank['currency'])

#----------------------------------------------------WORK----------------------------------------------

for index in range(4):
    print(index +1,':',banks[index]['name'])

select_bank = int(input('choose bank: '))
# print('Balance:')
# print(banks[select_bank]['balance'], banks[select_bank]['currency'])
if select_bank < 5 and select_bank >= 1:
    print(banks[select_bank - 1]['balance'],banks[select_bank - 1]['currency'])

else:
    print('Dont ruin my program! Go away!!!')





# for bank in banks:
#     print(bank['name'])


