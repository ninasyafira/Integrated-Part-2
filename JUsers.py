class JUsers():
    def __init__(self, username, account, password):
        self.__username = username
        self.__account = account
        self.__password = password

    def get_username(self):
        return self.__username
    def get_account(self):
        return self.__account
    def get_password(self):
        return self.__password

    def set_username(self, username):
        self.__username = username
    def set_account(self,  account):
        self.__account = account
    def set_password(self, password):
        self.__password = password

class Child():

    def __init__(self,parent,bank,month,year,child,account,amount):
        self.__parent = parent
        self.__child = child
        self.__account = account
        self.__amount = amount
        self.__bank = bank
        self.__month = month
        self.__year = year


    def get_parent(self):
        return self.__parent
    def get_child(self):
        return self.__child
    def get_account(self):
        return self.__account
    def get_amount(self):
         return self.__amount
    def get_bank(self):
         return self.__bank
    def get_month(self):
        return self.__month
    def get_year(self):
        return self.__year


    def set_parent(self, parent):
        self.__parent = parent
    def set_child(self, child):
        self.__child = child
    def set_account(self, account):
        self.__account = account
    def set_amount(self, amount):
        self.__amount =amount
    def set_bank(self, bank):
        self.__bank =bank
    def set_month(self, month):
        self.__month = month
    def set_year(self, year):
            self.__month = year