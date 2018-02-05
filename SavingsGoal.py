class SavingsGoal():
    def __init__(self, userid,type,setter, goal, duration,amount):
        self.__userid = userid
        self.__type = type
        self.__setter = setter
        self.__goal = goal
        self.__duration = duration
        self.__amount = amount

    def get_goal(self):
        return self.__goal
    def get_amount(self):
        return self.__amount
    def get_duration(self):
        return self.__duration
    def get_userid(self):
        return self.__userid
    def get_type(self):
        return self.__type
    def get_setter(self):
        return self.__setter


    def set_goal(self,goal):
        self.__goal = goal
    def set_amount(self,amount):
        self.__amount = amount
    def set_duration(self,duration):
        self.__duration = duration
    def set_userid(self,userid):
        self.__userid = userid
    def set_type(self,type):
        self.__type = type
    def set_setter(self,setter):
        self.__setter = setter
