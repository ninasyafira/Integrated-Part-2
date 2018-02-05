class rewardhistory():
    def __init__(self, userid, point, item, redeemdate, used):
        self.__userid = userid
        self.__point = point
        self.__item = item
        self.__redeemdate = redeemdate
        self.__used = used

    def get_userid(self):
        return self.__userid

    def get_point(self):
        return self.__point

    def get_item(self):
        return self.__item

    def get_redeemdate(self):
        return self.__redeemdate

    def get_used(self):
        return self.__used