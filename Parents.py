class Parents():
    def __init__(self, parentName, childName, ibank_user, ibank_password):
        self.__ibank_user = ibank_user
        self.__ibank_password =  ibank_password
        self.__childName = childName
        self.__parentName = parentName

    def get_ibank_user(self):
        return self.__ibank_user

    def get_ibank_password(self):
        return self.__savingAmount

    def get_childName(self):
        return self.__childName

    def get_parentName(self):
        return self.__parentName

    def set_ibank_password(self, ibank_password):
        self.__ibank_password = ibank_password

    def set_ibank_user(self, ibank_user):
        self.__ibank_user = ibank_user

    def set_childNamet(self, childName):
        self.__childName = childName

    def set_parentName(self, parentName):
        self.__parentName = parentName
