from spending import Spending
from datetime import datetime

def updateSpendLimit(name, month, year, newspendMax):
    print('updating.....')
    spendlist = []
    t_file = open('file/circlespendbarlimit.txt', 'r')
    spendMax = 0
    update = False
    monthMM = int(month)
    yearYY = int(year)
    for trans in t_file:
        list = trans.split(',')
        spendMax = int(list[3])
        if list[0] == name and int(list[1]) == yearYY and int(list[2]) == monthMM:
            print('updating =====')
            spendMax = newspendMax
            update = True
        writeline = '\n' + list[0] + ',' + list[1] + ',' + list[2] + ',' + str(spendMax) + '\n'
        spendlist.append(writeline)
    t_file.close()

    if update == True:
        print('updating ***')
        writeuser_file = open('file/circlespendbarlimit.txt', 'w')
        for userline in spendlist:
            writeuser_file.write(userline)
    elif update == False:
        print('adding')
        writeline = name + ',' + year + ',' + month + ',' + str(newspendMax) + '\n'
        writeuser_file = open('file/circlespendbarlimit.txt', 'a')
        writeuser_file.write(writeline)


def processPieChart(firstname, month):
    t_file = open('file/circlespendbar.txt', 'r')
    amount = 0
    for trans in t_file:
        list = trans.split(',')

    if list[0] == firstname and list[1] == month:
        # amount = (int(list[2])/2000)*100
        amount = int(list[2])
    return amount


def processSpendMax(name, month, year):
    spendlist = []
    t_file = open('file/circlespendbarlimit.txt', 'r')
    spendMax = 0
    for trans in t_file:
        list = trans.split(',')
        if list[0] == name and int(list[1]) == year and int(list[2]) == month:
            spendMax = int(list[3])
    return spendMax


def processSpend(name, month, year):
    spendlist = []
    t_file = open('file/spending.txt', 'r')

    for trans in t_file:
        list = trans.split(',')
        dateStr = list[2]
        dateDt = datetime.strptime(dateStr, '%Y-%m-%d')
        monthDt = dateDt.month
        yearDt = dateDt.year
        if list[0] == name and int(monthDt) == month and int(yearDt) == year:
            s = Spending(list[0], int(list[1]), list[2], list[3])
            spendlist.append(s)
    return spendlist