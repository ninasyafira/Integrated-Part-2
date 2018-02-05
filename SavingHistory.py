class SavingHistory():
    def __init__(self,user,type,name,goal,goalType,start,saving,saveDate):
        self.__user = user
        self.__type = type
        self.__name = name
        self.__goal = goal
        self.__goalType = goalType
        self.__start = start
        self.__saving = saving
        self.__saveDate = saveDate

    def get_user(self):
        return self.__user
    def get_type(self):
        return self.__type
    def get_name(self):
        return self.__name
    def get_goal(self):
        return self.__goal
    def get_goalType(self):
        return self.__goalType
    def get_start(self):
        return self.__start
    def get_saving(self):
        return self.__saving
    def get_saveDate(self):
        return self.__saveDate

    def set_user(self,user):
        self.__user = user
    def set_type(self,type):
        self.__type = type
    def set_name(self,name):
        self.__name = name
    def set_goal(self,goal):
        self.__goal = goal
    def set_goalType(self,goalType):
        self.__goalType = goalType
    def set_start(self,start):
        self.__start = start
    def set_saving(self,saving):
        self.__saving = saving
    def set_saveDate(self,saveDate):
        self.__saveDate = saveDate
