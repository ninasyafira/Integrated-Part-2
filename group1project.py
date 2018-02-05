from flask import Flask, render_template, request, session, flash, redirect, url_for
import mainprocessDaniel as mp
import Process
import MainProcess
import mainprocessEdmund as mpE
import AddGoalProcess
from wtforms import Form, StringField, SelectField, TextAreaField, RadioField, PasswordField, validators, IntegerField, TextField
from datetime import datetime
import datetime
from wtforms.validators import ValidationError
import SavingsGoal
import time
import Goal



app = Flask(__name__)


class RegisterChild(Form):
    parent = StringField('Parent Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    bank = StringField('Parent Bank Number', [validators.Length(min=1, max=150), validators.DataRequired()])
    child= StringField('Child Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    account = StringField('Child Saving Account Number', [validators.Length(min=1, max=150), validators.DataRequired()])
    amount = StringField('Saving Amount', [validators.Length(min=1, max=150), validators.DataRequired()])


class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])



@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        P = MainProcess.validate_User(username, password)
        if P == True:
            session['userid'] = username
            return redirect(url_for('afterlogin'))
        else:
            error = 'Invalid login'
            flash(error, 'danger')
            return redirect(url_for('login'))

            # return render_template('login.html', form=form)

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

@app.route('/registerchild' ,methods=['GET', 'POST'])
def registerchild():
    form = RegisterChild(request.form)
    if request.method == 'POST' and form.validate():
        MainProcess.registerNewChild(form.parent.data, form.bank.data, form.child.data, form.account.data,
                                     form.amount.data)
        print("Child Successfully Register")
        return redirect(url_for('pctransaction'))
    return render_template('registerchild.html', form=form)



@app.route('/pc',methods=['GET', 'POST'])
def pctransaction():

    userslist = []
    userslist = MainProcess.processUser(session['userid'])

    totalDeposit = 0
    totalDeposit = MainProcess.processTransaction(session['userid'], MainProcess.current_Month(), 'deposit')

    return render_template('pctransaction.html',child=userslist, count=len(userslist),
                           totalDepositAmount = totalDeposit, monthNow= MainProcess.current_Month(),
                          monthPrev =MainProcess.previous_Month(), TEST= MainProcess.TEST(session['userid']),userS = session['userid'])


@app.route('/editamount',methods=['GET', 'POST'])
def editamount():
    form = RegisterChild(request.form)
    class NewLimit(Form):
        childName = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
        monthlylimit = StringField('Amount', [validators.Length(min=1, max=150), validators.DataRequired()])

    form = NewLimit(request.form)
    if request.method == 'POST' and form.validate():
        MainProcess.updateAmount(session['userid'], form.childName.data, form.monthlylimit.data)
        print('Success')
        return redirect(url_for('pctransaction'))
    return render_template('editamount.html', form=form,user = session['userid'])

@app.route('/deletechild', methods=['GET','POST'])
def delete():
    form = RegisterChild(request.form)

    class NewLimit(Form):
        childName = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])

    form = NewLimit(request.form)
    if request.method == 'POST' and form.validate():
        MainProcess.deleteChild(form.childName.data)
        print('Delete Success')
        return redirect(url_for('pctransaction'))
    return render_template('deletechild.html', form=form,userS = session['userid'])



@app.route('/afterlogin' , methods=['GET', 'POST'])
def afterlogin():
    form = MonthForm(request.form)
    if request.method == 'POST' and form.validate():
        monthMM = form.month.data
        checkMonth = int(monthMM)
        print(monthMM)

    now = datetime.datetime.now()
    todayMonth = now.month
    todayYear = now.year
    months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December')

    if todayMonth == 2:
        prevMonth = 1
    else:
        prevMonth = todayMonth - 1

    if todayYear == 2018 :
        prevYear = 2017
    else :
        prevYear = now.year - 1

    usersList = []
    usersList = Process.processUser(session['userid'],todayMonth)
    savings = []
    limit = []
    limit = Process.limit(session['userid'],todayMonth)
    over = Process.over(session['userid'],todayMonth)
    displayHistory = []
    #displayHistory = Process.displayHistory(session['userid'],goalType)

    return render_template('homepage.html', users=usersList,checkMM=months[todayMonth],saving=savings,todayMonth=todayMonth, prevMonth=prevMonth, todayYear=todayYear, prevYear=prevYear,limits=limit,over=over,form=form,userS = session['userid'],displayHistory=displayHistory)


class MonthForm(Form):
    month = SelectField('Month', [validators.DataRequired()],
                           choices=[('0', 'Select'),('2','February 2018'),('1','January 2018'), ('12', 'December 2017'), ('11', 'November 2017'),
                                    ('10', 'October 2017'), ('9', 'September 2017'), ('8', 'August 2017'), ('7', 'July 2017')],
                           default='')

@app.route('/selected', methods=['GET', 'POST'])
def selected():

    now = datetime.datetime.now()
    todayMonth = now.month
    todayYear = now.year
    if todayMonth == 1:
        prevMonth = 12
    else :
        prevMonth = todayMonth - 1

    if todayYear == 2018 :
        prevYear = 2017
    else :
        prevYear = now.year - 1

    form = MonthForm(request.form)
    if request.method == 'POST' and form.validate():
        monthMM = form.month.data
        checkMonth = int(monthMM)
        print(monthMM)

        months = ('Null','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December')

        usersList = []

        usersList = Process.processUser(session['userid'],checkMonth)
        limit = []
        limit = Process.limit(session['userid'], checkMonth)
        over = Process.over(session['userid'], checkMonth)

        return render_template('selected.html',users=usersList,checkMM=months[checkMonth], count=len(usersList),limits=limit,over=over,form=form,userS = session['userid'])


@app.route('/updateNina/<string:postlist>/',methods=['GET','POST'])
def update_savingHistory(postlist):
    #session['userid'] = 'Mary'

    print('==========================================')
    print(postlist)
    print('==========================================')
    plist = postlist.split('$')
    name = plist[0]
    goalType = plist[1]
    displayHistory = []
    displayHistory = Process.displayHistory(session['userid'],goalType)
    #print(displayHistory)

    now = datetime.datetime.now()
    todayMonth = now.month
    checkMonth = now.month
    todayYear = now.year

    #form = MonthForm(request.form)

    usersList = []
    usersList = Process.processUser(session['userid'],checkMonth)
    limit = []
    limit = Process.limit(session['userid'], checkMonth)
    over = Process.over(session['userid'], checkMonth)

    checkMM = 2
    prevMonth = 1
    prevYear = 2017

    form = MonthForm(request.form)

    print('*************************************')
    print(postlist)
    print('**********************************')
    return render_template('nov.html',users=usersList,checkMM=checkMM,limits=limit,over=over,user=name,displayHistory=displayHistory,form=form,userS = session['userid'])
    #return redirect(url_for('afterlogin'))

@app.route('/promo')
def promo():
    session['userid'] = 'Alex'
    todayDate = datetime.today()
    todayMonth = todayDate.month
    todayYear = todayDate.year
    todayLong = todayDate.strftime('%d-%B-%Y  %H:%M:%S')
    promolist = mp.processPromo()

    return render_template('promo.html', promolist = promolist, todayDt=todayLong)


@app.route('/rewards')
def rewards():

    userpoint = mp.processuser_point(session['userid'])

    userlist = []
    userlist = mp.processuser_rewards(session['userid'])

    rewardlist = []
    rewardlist = mp.processavail_rewards(userpoint)

    return render_template('rewards.html', users=userlist, rewards=rewardlist, count=len(userlist),userS=session['userid'],userpoint=userpoint)


@app.route('/updateDaniel/<string:postlist>/', methods=['GET', 'POST'])
def update_userReward(postlist):

    print(postlist)
    plist = postlist.split('$')
    itemdesc = plist[0]
    userid = plist[1]
    itemdeduct = plist[2]

    print('==================')
    print(itemdesc)
    print(userid)
    print(itemdeduct)
    #if request.method == 'POST':
    mp.addNewUserRedeemReward(userid, itemdesc, itemdeduct)
    print("User Successfully Register")

    userpoint = mp.processuser_point(userid)
    userlist = []
    userlist = mp.processuser_rewards(userid)
    rewardlist = []
    rewardlist = mp.processavail_rewards(userpoint)
    return render_template('rewards.html', users=userlist, rewards=rewardlist, count=len(userlist),userid=userid,userpoint=userpoint,userS = session['userid'])

class RegisterIdea(Form):
    rewardidea = StringField('Reward Idea', [validators.Length(min=1, max=500), validators.DataRequired()])

@app.route('/forms', methods=['GET', 'POST'])
def ideaform():
    form = RegisterIdea(request.form)
    if request.method == 'POST' and form.validate():
        mp.registerNewIdea(form.rewardidea.data)
        print("Idea has been registered!")
        flash('Idea has been submitted succesfully. Thank you for your idea!', 'success')
        # return redirect(url_for('rewards'))
        form.rewardidea.data = ''
        return render_template('form.html', form=form,userS = session['userid'])

    return render_template('form.html', form=form,userS = session['userid'])


class Formforsession(Form):
    userlist = []
    user = open('file/addgoals.txt', 'r')
    for userid in user:
        list = userid.split(',')
        if list[0] not in userlist:
            userlist.append(list[0])
    print(userlist)
    usersession = SelectField('',[validators.DataRequired()], choices=[('0','Select'),('John', userlist[0]),('Amy',userlist[1]),('All',userlist[0][1])],default='')

class monthForm(Form):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']

    year = ['2018','2017','2016']

    month = SelectField('Month', [validators.DataRequired()],choices=[('0', 'Select'),('1','January'),
                                                                      ('2','February'),('3,','March'),
                                                                      ('3','April'), ('4','May'),
                                                                      ('5','June'), ('6','July'),
                                                                      ('7','August'), ('8','September'),
                                                                      ('9','October'),('10','November'),
                                                                      ('11','December')],default='')
    currYear = datetime.datetime.now().date().year
    past1Year = (datetime.datetime.now().date() - datetime.timedelta(days=365)).year
    past2Year = (datetime.datetime.now().date() - datetime.timedelta(days=750)).year
    past3Year = (datetime.datetime.now().date() - datetime.timedelta(days=3*365)).year

    years = SelectField('Year', [validators.DataRequired()], choices=[('0', 'Select'),('1',currYear),('2',past1Year),('3',past2Year),('4',past3Year)])



@app.route('/mk' , methods=['GET', 'POST'])
def mk():
    userlist = []
    user = open('file/addgoals.txt', 'r')
    for userid in user:
        list = userid.split(',')
        if list[0] not in userlist:
            userlist.append(list[0])

    form = Formforsession(request.form)
    if request.method == 'POST' and form.validate():
        usersession = form.usersession.data
        if usersession == userlist[0]:
            session['userid'] = userlist[0]
        elif usersession == userlist[1]:
            session['userid'] = userlist[1]
        elif usersession == userlist[2]:
            session['userid'] = userlist[2]
        elif usersession == userlist[3]:
            session['userid'] = userlist[3]

    userslist = []
    userslist = AddGoalProcess.processUser(session['userid'])

    countList = []
    countList = AddGoalProcess.countUser(session['userid'])

    savingslist = []
    savingslist = AddGoalProcess.processSavings(session['userid'])

    useridlist = AddGoalProcess.userslist()

    form2 = monthForm(request.form)
    if request.method == 'POST' and form2.validate():
        monthMM = form2.month.data
        yearMM = form2.years.data
        checkMonth = int(monthMM)
        checkYear = int(yearMM)

        datelist = []
        user = open('file/addgoals.txt', 'r')
        for userid in user:
            list = userid.split(',')
            if list[4] not in datelist:
                datelist.append(list[4])
        print(datelist)
        now = datetime.datetime.now()
        todayMonth = now.month
        todayYear = now.year


    months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December')
    return render_template('Goals.html', form = form, users = userslist, count=len(userslist), user = userlist,
                           savings = savingslist, countSavings = len(savingslist), countList = len(countList),
                           usersid = useridlist, months = months, form2 = form2,userS = session['userid'])

@app.route('/homeupdated' , methods=['GET', 'POST'])
def homeselected():
    now = datetime.datetime.now()
    todayMonth = now.month
    todayYear = now.year

    now = datetime.datetime.now()
    todayMonth = now.month
    todayYear = now.year
    months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December')
    datelist = []
    user = open('file/addgoals.txt', 'r')
    for userid in user:
        list = userid.split(',')
        if list[4] not in datelist:
            datelist.append(list[4])
    print(datelist)

    form2 = monthForm(request.form)
    if request.method == 'POST' and form2.validate():
        monthMM = form2.month.data
        yearMM = form2.years.data
        checkMonth = int(monthMM)
        print(monthMM)

    userslist = []
    userslist = AddGoalProcess.processUser(session['userid'])

    countList = []
    countList = AddGoalProcess.countUser(session['userid'])

    savingslist = []
    savingslist = AddGoalProcess.processSavings(session['userid'])

    useridlist = AddGoalProcess.userslist()

    return render_template('Goals.html', users=userslist, count=len(userslist), user=userslist,
                           savings=savingslist, countSavings=len(savingslist), countList=len(countList),
                           usersid=useridlist, months=months, form2 = form2,userS = session['userid'])


@app.route('/update/<string:id>', methods=['GET', 'POST'])
def update(id):
    print(id)
    list = id.split('$')
    userid = list[0]
    setter = list[1]
    goal= list[2]

    userlist = []
    user_file = open('file/addgoals.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        if list[0] == userid and list[2] == setter and list[3] == goal:
            usergoal = Goal.Goal(list[0],list[1],list[2],list[3],list[4],list[5])
            userlist.append(usergoal)
    user_file.close()

    form = RegisterUpdateUser(request.form)
    if request.method == 'POST' and form.validate():
        if form.type.data =="parent":
            userid = form.userid.data
            type = form.type.data
            setter = form.setter.data
            goal = form.goal.data
            amount = form.amount.data
            duration = form.duration.data
            userlist3 = []
            userlist3 = AddGoalProcess.EditUser(setter,goal,amount,duration)
            #update addgoals.txt

            #AddGoalProcess.registerNewUser(parentgoal.get_userid(),parentgoal.get_type(),parentgoal.get_setter(),parentgoal.get_goal(),parentgoal
                                        #.get_amount(),parentgoal.get_duration())

            print("Goal Parent successfully Updated")
            flash("Goal Parent successfully Updated")

        elif form.type.data =="child":
            userid = form.userid.data
            type = form.type.data
            setter = form.setter.data
            goal = form.goal.data
            amount = form.amount.data
            duration = form.duration.data
            userlist3 = []
            userlist3 = AddGoalProcess.EditUser(setter, goal, amount, duration)

            #AddGoalProcess.registerNewUser(childgoal.get_userid(),childgoal.get_type(),childgoal.get_setter(),childgoal.get_goal(),childgoal.get_amount(),
                                        # childgoal.get_duration())


            print("Goal Child successfully Updated")
            flash("Goal Child successfully Updated")
        return redirect(url_for('home'))
    else:
        #userlist3 = []
        #userlist3 = AddGoalProcess.EditUser(userid,setter,goal,form)
        for goal in userlist:
            print(goal.get_userid()+"$"+goal.get_setter()+"$"+goal.get_goal())
            print(id)
            if (goal.get_userid()+"$"+goal.get_setter()+"$"+goal.get_goal()) == id:
                print("success")
                form.userid.data = goal.get_userid()
                form.type.data = goal.get_type()
                form.setter.data = goal.get_setter()
                form.goal.data = goal.get_goal()
                form.amount.data = goal.get_amount()
                form.duration.data = goal.get_duration()
            #goal = Goal.Goal(list[0], list[1], list[2], list[3], list[4], list[5])
        form.userid.data = goal.get_userid()
        form.type.data = goal.get_type()
        form.setter.data = goal.get_setter()
        form.goal.data = goal.get_goal()
        form.amount.data = goal.get_amount()
        form.duration.data = goal.get_duration()

        return render_template('EditGoal.html',form = form,userS = session['userid'])


@app.route('/delete_goal/<string:id>', methods=['GET','POST'])
def delete_goal(id):

    print('hello')
    print(id)
    list = id.split('$')
    userid = list[0]
    setter = list[1]
    goal = list[2]

    userslist2 = []
    userslist2 = AddGoalProcess.updateUser(userid,setter,goal)

    session['userid'] = 'John'
    userlist = []
    user = open('file/addgoals.txt', 'r')
    for userid in user:
        list = userid.split(',')
        if list[0] not in userlist:
            userlist.append(list[0])

    form = Formforsession(request.form)
    if request.method == 'POST' and form.validate():
        usersession = form.usersession.data
        if usersession == '0':
            session['userid'] = usersession
        elif usersession == '1':
            session['userid'] = usersession
    userslist = []
    userslist = AddGoalProcess.processUser(session['userid'])

    countList = []
    countList = AddGoalProcess.countUser(session['userid'])

    savingslist = []
    savingslist = AddGoalProcess.processSavings(session['userid'])

    useridlist = AddGoalProcess.userslist()
    form2 = monthForm(request.form)
    if request.method == 'POST' and form2.validate():
        monthMM = form2.month.data
        yearMM = form2.years.data
        checkMonth = int(monthMM)
        checkYear = int(yearMM)

        datelist = []
        user = open('file/addgoals.txt', 'r')
        for userid in user:
            list = userid.split(',')
            if list[4] not in datelist:
                datelist.append(list[4])
        print(datelist)
        now = datetime.datetime.now()
        todayMonth = now.month
        todayYear = now.year

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']




    flash('Your %s Goal Successfully Deleted'%(goal), 'success')
    return render_template('Goals.html', form = form, users = userslist, count=len(userslist), user = userlist,
                           savings = savingslist, countSavings = len(savingslist),form2 = form2,
                           usersid = useridlist, months = months, users2 = userslist2, countList = len(countList),userS = session['userid'])

#for AddGoal.html
class RegisterUpdateUser(Form):
    userlist = []
    user = open('file/addgoals.txt', 'r')
    for userid in user:
        list = userid.split(',')
        if list[0] not in userlist:
            userlist.append(list[0])

    userid = SelectField('Name ',[validators.DataRequired()],choices =[('John','John'),('Amy','Amy')])
    type = SelectField('Parent or Child ',[validators.DataRequired()], choices=[('parent', 'Parent'), ('child', 'Child')])
    setter = StringField('Name of Setter (Alphabets + numbers) ', [validators.Length(min=1, max=150), validators.DataRequired()])
    goal = StringField('Goal', [validators.Length(min=1, max=150), validators.DataRequired()])
    amount = StringField('Amount in $', [validators.Length(min=1, max=152), validators.DataRequired(),])
    duration = StringField('Duration in Days', [validators.Length(min=1, max=152), validators.DataRequired()])

@app.route('/AddGoal', methods=['GET', 'POST'])
def AddGoal():
    userslist = []
    userslist = AddGoalProcess.processUser(session['userid'])

    useridlist = AddGoalProcess.userslist()

    form = RegisterUpdateUser(request.form)
    if request.method == 'POST' and form.validate():
        if form.type.data =="parent":
            userid = form.userid.data
            type = form.type.data
            setter = form.setter.data
            goal = form.goal.data
            amount = form.amount.data
            duration = form.duration.data
            AddGoalProcess.registerNewUser(userid,type,setter,goal,amount,duration)
            print("Goal Parent Successfully Added")
            flash("Goal Parent Suddessfully Added","success")

        elif form.type.data =="child":
            userid = form.userid.data
            type = form.type.data
            setter = form.setter.data
            goal = form.goal.data
            amount = form.amount.data
            duration = form.duration.data
            AddGoalProcess.registerNewUser(userid,type,setter,goal,amount,duration)
            print("Goal Child Successfully Added")
            flash("Goal Child Suddessfully Added", "success")

    return render_template('AddGoals.html', form=form,users = userslist,count=len(userslist),usersid = useridlist,userS = session['userid'])


def validate_monthStr(form,field):
    print('validate month')
    print(field.data)
    if int(field.data)>12 or int(field.data)<1:
        print('error')
        raise ValidationError('error: !!!!!! month is wrong')

class SpendForm(Form):
    monthStr = StringField('Month', [validators.Length(min=1, max=12), validators.DataRequired(),validate_monthStr])
    yearStr = StringField('Year', [validators.Length(min=1, max=2018), validators.DataRequired()])

class Form2(Form):
    month = StringField('Month', [validators.Length(min=1, max=150), validators.DataRequired()])
    year = StringField('Year', [validators.Length(min=1, max=150), validators.DataRequired()])
    limit = StringField('Spend Limit', [validators.Length(min=1, max=150), validators.DataRequired()])

@app.route('/checkspend', methods=['GET', 'POST'])
def checkspend():

    today = datetime.datetime.today()
    monthMM=today.month
    yearYY=today.year

    form = SpendForm(request.form)
    formlimit = Form2(request.form)

    if request.method == 'POST' and form.validate():
        monthMM = form.monthStr.data
        yearYY = form.yearStr.data
        print(monthMM)

    todayDate = datetime.datetime.today()
    todayMonth = todayDate.month
    todayYear = todayDate.year
    todayLong = todayDate.strftime('%d-%B-%Y %H:%M:%S')
    monthDesc = ('null', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    print(monthDesc[1])

    spendlist = []
    for s in spendlist:
        print(s)

    checkMonth = int(monthMM)
    checkYear = int(yearYY)
    spendMax = mpE.processSpendMax(session['userid'], checkMonth, checkYear)
    print(spendMax)

    spendlist = mpE.processSpend(session['userid'], checkMonth, checkYear)
    spendtotal = 0
    for s in spendlist:
        print(s)
        spendtotal += s.get_amount()
    print(spendtotal)

    return render_template('checkspenddetails.html', checkMM=monthDesc[checkMonth], checkYY=checkYear,
                       spendings=spendlist, count=len(spendlist), todayDate=todayLong, spendmax=spendMax,
                       spendtotal=spendtotal,
                       form=form, formlimit=formlimit,userS = session['userid'])

@app.route('/formlimit', methods=['POST'])
def formlimit():

    today = datetime.datetime.today()
    monthMM=today.month
    yearYY=today.year

    form = SpendForm(request.form)
    formlimit = Form2(request.form)

    if request.method == 'POST' and formlimit.validate():
        print('mm')
        limitMM = formlimit.month.data
        limitYY = formlimit.year.data
        limitAmt = formlimit.limit.data

    todayDate = datetime.datetime.today()
    todayMonth = todayDate.month
    todayYear = todayDate.year
    todayLong = todayDate.strftime('%d-%B-%Y %H:%M:%S')
    monthDesc = ('null', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    print(monthDesc[1])

    mpE.updateSpendLimit(session['userid'], limitMM, limitYY, limitAmt)

    spendlist = []
    for s in spendlist:
        print(s)

    checkMonth = int(monthMM)
    checkYear = int(yearYY)
    spendMax = mpE.processSpendMax(session['userid'], checkMonth, checkYear)
    print(spendMax)

    spendlist = mpE.processSpend(session['userid'], checkMonth, checkYear)
    spendtotal = 0
    for s in spendlist:
        print(s)
        spendtotal += s.get_amount()
    print(spendtotal)

    return redirect(url_for('checkspend'))




@app.route('/pie')
def spending():
    spending = mpE.processPieChart(session['userid'], 'Nov')
    print(spending)
    return render_template('pc2a.html')


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run()

def validation_userid(form,field):
    if field.data.isalpha():
        form.userid.data = form.userid.data
    else:
        raise ValidationError('UserID must be a string')

    for i in form.setter.data:
        if i.isalnum():
            form.setter.data = form.setter.data
        else:
            raise ValidationError('Your Name must contain a string and a number')

    if form.goal.data.isalpha():
        form.goal.data = form.goal.data
    else:
        raise ValidationError('Name of your goal must be a string')

    if form.amount.data.isdigit():
        form.amount.data = form.amount.data
    else:
        raise ValidationError('')

    if form.duration.data.isdigit():
        form.duration.data = form.duration.data
    else:
        raise ValidationError('Your duration must an integer')

    if int(form.duration.data) <1:
        raise ValidationError('Your length of duration must be at least 1 day')