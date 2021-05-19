
curs = {
    "EUR": 101.65,
    "USD": 84.80,
    "RUB": 1.13,
}

def convert(money,val):
    result = money / curs[val]
    print(val,':', result)
    

val = input('Currency: ')
money = float(input('change to som: '))


if curs.get(val) != None:
    convert(money,val)

else:
    print('ERROR!!')

convert(money,val)



print(f"USD {1 * 84.80} SOM")
# print(f"35 days are {35 * 24 * 60 * 60} SOM")
# print(f"50 days are {50 * 24 * 60 * 60} SOM")
# print(f"110 days are {110 * 24 * 60 * 60} SOM") 





