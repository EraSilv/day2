import crypt
aa = ' '

class Client:
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.__password = password
    
    def set_password(self, aa):
        aa = input('input password: ')
        if len(aa) < 8:
            print("Password must be at least 8 characters")
        else:
            self.__password = aa
            self.password = aa

    def get_password(self):
        return 'шифрованный'
    
    def raw_password(self, ps):
        print('никому не рассказывайте пароль!')
        return self.__password
        



# Интернет магазин bootcamp
# наш клиент
adam = Client('Adam', 'adam', 1994 )


#change Client password
adam.set_password(aa)



#get secr password
print(adam.get_password())

#private action for admins
print(adam.raw_password(aa))