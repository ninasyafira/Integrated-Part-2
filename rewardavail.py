class avail_rewards():
    def __init__(self, number, reward, deduct):
        self.__number = number
        self.__reward = reward
        self.__deduct = deduct

    def get_number(self):
        return self.__number
    def get_reward(self):
        return self.__reward
    def get_deduct(self):
        return self.__deduct

    def set_number(self, number):
        self.__number = number
    def set_reward(self, reward):
        self.__reward = reward
    def set_deduct(self, deduct):
        self.__deduct = deduct