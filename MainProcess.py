from JUsers import JUsers
from JUsers import Child
from datetime import *

months = ["Unknaown","January","Febuary","March","April","May","June","July","August","September","October","November","December"]

now = (datetime.now())
year = (now.year)
month = (months[now.month])
print(month)

def current_Month():
    return month

def previous_Month():
    return months[now.month-1]

def processUser(parent):
    usersList = []
    user_file = open('file/child.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        print(list)
        s= Child(list[0], list[1],list[2],list[3],list[4],list[5],int(list[6]))
        if list[0] == parent:
         usersList.append(s)
    return usersList

def processTransaction(parent, month, type='deposit'):
    t_file = open('file/child.txt', 'r')
    total = 0
    for trans in t_file:
        list = trans.split(',')

        if list[0] == parent and list[2] == month:
            total += float(list[6])
    return total

def registerNewUser(username, account, password):
    userdata = username + ',' + account +',' + password +'\n'
    user_file = open('file/login.txt', 'a')
    user_file.write(userdata)

def validate_User(username, password):
    #usersList = []
    user_file =open('file/login.txt','r')
    for ulist in user_file:
        list = ulist.split(',')
        print(list)
        #usersList.append(list)
        if username == list[0] and (password + '\n') == list[2]:
            return True

def registerNewChild(parent,bank,child, account, amount):
    userdata = parent + ',' +bank+','+str(month) +','+str(year) +','+child +','+ account +',' + str(amount) +'\n'
    user_file = open('file/child.txt', 'a')
    user_file.write(userdata)
    ninadata = parent + ','


def TEST(name):
    List = []
    user_file = open('file/child.txt', 'r')
    for i in user_file:
        list = i.split(',')
        if list[0] == name:
            List.append(list[4])

    return List

def updateAmount(name, childName, limit):
    with open('file/child.txt', 'r') as file:
        newline = []
        for word in file:
            word = word.strip()
            s = word.split(',')
            if name == s[0] and childName == s[4]:
                print("success x2")
                newline.append(word.replace(s[6], limit))
            else:
                newline.append(word)

    with open('file/child.txt', 'w') as file:
        for line in newline:
            file.write(line + '\n')

def deleteChild(childName):
    temporary_list = []
    user_file = open('file/child.txt', 'r')
    for item in user_file:
        list = item.split(',')
        s = Child(list[0], list[1], list[2], list[3], list[4], list[5], int(list[6]))
        temporary_list.append(s)

    list = []
    for item in temporary_list:
        if item.get_child() != childName:
            s = "%s,%s,%s,%s,%s,%s,%d,\n" %(item.get_parent(),item.get_bank(),item.get_month(),item.get_year(),item.get_child(),item.get_account(),item.get_amount())
            list.append(s)
    user_file = open('file/child.txt','w')
    for i in list:
        user_file.write(i)
    user_file.close()


def diffMonths(prevMonth,currMonth,prevYear,currYear):

    currMonth = datetime.now().month
    currYear = datetime.now().year