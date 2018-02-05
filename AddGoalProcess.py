from Goal import Goal
from SavingsGoal import SavingsGoal
from datetime import datetime


def processUser(userid):
    usersList = []
    user_file = open('file/addgoals.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        if list[0] == userid:
            s = Goal(list[0], list[1], list[2], list[3], int(list[4]), int(list[5]),list[6],list[7],list[8])
            usersList.append(s)
    return usersList

def countUser(userid):
    countList = []
    user_file = open('file/addgoals.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        if list[0] == userid and list[6] =='A':
            s = Goal(list[0], list[1], list[2], list[3], int(list[4]), int(list[5]),list[6],list[7],list[8])
            countList.append(s)
    return countList


def updateUser(userid,setter,goal):
    usersList = []
    user_file = open('file/addgoals.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        status = list[6]
        if list[0] == userid and list[2] == setter and list[3] == goal:
            status = 'D'
        writeline = list[0] + ',' + list[1] + ',' + list[2]+ ',' + list[3]+ ',' + list[4]+ ',' + list[5]+ ','+ status + ',' + 'x' + ',' + 'a' + '\n'
        usersList.append(writeline)

    writeuser_file = open('file/addgoals.txt', 'w')
    for userline in usersList:
        writeuser_file.write(userline)

    return usersList

def EditUser(newsetter,newgoal,newamount,newduration):
    usersList = []
    user_file = open('file/addgoals.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        setter = list[2]
        goal = list[3]
        amount = list[4]  #original amount
        duration = list[5]
        if list[2] == setter and list[3] == goal and list[4] == amount and list[5] == duration:
            setter = newsetter
            goal = newgoal
            amount = newamount
            duration = newduration
        writeline = list[0] + ',' + list[1] + ',' + setter + ',' + goal +',' + amount +',' + duration + ','+ list[6] + ',' + 'x' + ',' + 'a' +'\n'
        usersList.append(writeline)

    writeuser_file = open('file/addgoals.txt', 'w')
    for userline in usersList:
        writeuser_file.write(userline)
    writeuser_file.close()

    return usersList



def processSavings(userid):
    usersList = []
    user_file = open('file/savegoals.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        if list[0] == userid:
            s = SavingsGoal(list[0], list[1], list[2], list[3], list[4], int(list[5]))
            usersList.append(s)
    return usersList


def registerNewUser(name,type,setter,goal,amount,duration,status='A',val = 'x',str = 'a'):
    userdata = name + ',' + type + ','+ setter + ',' + goal + ',' + amount + ',' + duration + ',' + status + ','+ val +',' + str + '\n'
    user_file = open('file/addgoals.txt', 'a')
    user_file.write(userdata)


def updateCurrentUser(name,type,setter,goal,amount,duration):
    userdata = name + ',' + type + ','+ setter + ',' + goal + ',' + amount + ',' + duration + '\n'
    user_file = open('file/addgoals.txt', 'a')
    user_file.write(userdata)

def userslist():
    userlist = []
    user = open('file/savegoals.txt','r')
    for userid in user:
        list = userid.split(',')
        if list[0] not in userlist:
            userlist.append(list[0])
    return userlist


def checkdate(date):
    user = open('file/savegoals.txt', 'r')
    for userid in user:
        list = userid.split(',')
        ddmmyyyy = list
        if list[2] > date :
            print('Your goal has expired!')
        elif list[2] == date:
            print('Your goal is expiring today!')
        else:
            print('Remember to save up for your goals!')
