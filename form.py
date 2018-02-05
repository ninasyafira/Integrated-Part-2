from flask import Flask, render_template, request, session
from wtforms import Form, StringField, validators

import danielmainprocess

class RegisterIdea(Form):
    rewardidea = StringField('rewardidea', [validators.Length(min=1, max=500), validators.DataRequired()])

@app.route('/rewardsDaniel.html', methods=['GET', 'POST'])
def home():
    session['userid'] = 'Alex'
    form = RegisterIdea(request.form)
    if request.method == 'POST' and form.validate():
        danielmainprocess.registerNewIdea(form.rewardidea.data)
        print("Your idea has been registered!")

    return render_template('/rewardsDaniel.html', form=form)