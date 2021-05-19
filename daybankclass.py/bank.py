import random
class Bank:
    def __init__(self,bank_name, bank_balance):
        self.bank_name = bank_name
        self.bank_balance = bank_balance



    def bank_info(self):
        print('Welcome to : ' , self.bank_name)


    def create_account(self, client_name,password):
        pandom = random.randint(1000 , 2000)
        self.accounts = {
            pandom: {
                'name': client_name,
                'password': password,
                'balance' : 0

            }
        }
        print(
            'Ваш аккаунт открыт:','\n',
            'Имя: ',self.accounts[pandom]['name'],'\n',
            'Пароль: ',self.accounts[pandom]['password'],'\n',
            'Баланс: ',self.accounts[pandom]['balance'],'\n',
        )
        print('Счет вашего аккаунта:', pandom)
        return pandom



    def get_acc(self,number):
        print('Ur account: ' , self.accounts[number])


    def get_bank_balance(self):
        print('Cash: ' , self.bank_balance)





    def get_balance(self,number):
        print('Деньги на вашем счете:',self.accounts[number]['balance'])
        


    def create_card(self,client_name):
        pass

    def add_money_to_balance(self,number,money):
        self.accounts[number]['balance'] = self.accounts[number]['balance']+money
        print('Ur money was increased till : ' , money)





    def create_card(self, client_name, type, password):
        pass





    def get_credits_card(self, client_name):
        pass

