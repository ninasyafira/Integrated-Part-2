from rewardavail import avail_rewards
from rewardhistory import rewardhistory
from datetime import datetime

## import user reward information
def processuser_point(userid):
    userpoint = 0
    avail_file = open('file/rewardhistory.txt', 'r')
    for ulist in avail_file:
        list = ulist.split(',')
        if list[0] == userid:
            userpoint = list[1]
    return userpoint

def processuser_rewards(userid):
    userList = []
    avail_file = open('file/rewardhistory.txt', 'r')
    for ulist in avail_file:
        list = ulist.split(',')
        if list[0] == userid:
            s = rewardhistory(list[0], int(list[1]), list[2], list[3], list[4])
            userList.append(s)
    return userList

def processavail_rewards(userpoint):
    rewardsavailList = []
    avail_file = open('file/rewardavail.txt', 'r')
    for ulist in avail_file:
        list = ulist.split(',')
        if int(list[2]) <= int(userpoint):
        #if int(list[2]) <= 10000:
            s = avail_rewards(list[0], list[1], int(list[2]))
            rewardsavailList.append(s)
    return rewardsavailList

def addNewUserRedeemReward(userid,itemdesc,itemdeduct):
    print('test')
    print(userid)
    print(itemdesc)

    #get today date
    todayDate=datetime.today()
    todayDt=todayDate.strftime('%Y-%m-%d')
    print(todayDt)

    #get user points
    userlist = []
    userpoint = 0
    loginuserpoint = 0
    user_file = open('file/users.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        userpoint = int(list[2])    #current user point
        if list[0] == userid:   #if user is found, deduct his user point, otherwise skip for other users
            userpoint = userpoint - int(itemdeduct)
            loginuserpoint = userpoint
        writeline = list[0] + ',' + list[1] + ',' + str(userpoint) + '\n'
        userlist.append(writeline)

    #update rewardhistory.txt
    userdata = userid + ',' + str(loginuserpoint) +',' + itemdesc +',' + todayDt + ',' + 'No' +'\n'
    #userdata = 'xxx,100,yyyyyy,2018-01-12,Y' + '\n'
    avail_file = open('file/rewardhistory.txt', 'a')
    avail_file.write(userdata)

    #update users.txt - user's new point after deduction becose of redeemption
    writeuser_file = open('file/users.txt', 'w')
    for userline in userlist:
        writeuser_file.write(userline)

import tkinter
import tkinter.messagebox

class CallbackDemo:
   def __init__(self):
       self.main_window = tkinter.Tk()
       self.button = tkinter.Button(self.main_window, text='Click', command=self.display)
       self.button.pack()
       tkinter.mainloop()

   def display(self):
       tkinter.messagebox.showinfo('Response', 'Thank you for your idea!')



def registerNewIdea(rewardidea):
    ideadata = str(rewardidea) + '\n'
    idea_file = open('file/rewardidea.txt', 'a')
    idea_file.write(ideadata)
    CallbackDemo()