import bank
Bai_Tushum = bank.Bank(bank_name= 'Bai_Tushum' , bank_balance= 369_542_130.00)
Bai_Tushum.bank_info()
Bai_Tushum.get_bank_balance()





number = Bai_Tushum.create_account(
    client_name= 'Era',
    password= 123456

)

print('I got number:', number)


Bai_Tushum.add_money_to_balance(number,651323)
Bai_Tushum.add_money_to_balance(number,15613)

Bai_Tushum.get_acc(number)






