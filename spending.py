class Spending():
    def __init__(self, userid, amount, datespend, item):
        self.__userid = userid
        self.__amount = amount
        self.__datespend = datespend
        self.__item = item

    def get_userid(self):
        return self.__userid

    def get_amount(self):
        return self.__amount

    def get_datespend(self):
        return self.__datespend

    def get_item(self):
        return self.__item

    def __str__(self):
        return '%s %s' % (self.__amount, self.__item)