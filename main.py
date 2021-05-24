
from flask import Flask,render_template,request


#form import 
from flask_wtf import FlaskForm


#form butoton import 
from wtforms.fields import *


#form validator 
from wtforms.validators import DataRequired



app=Flask(__name__)


#form key   
app.config['SECRET_KEY']='mclkjllcjvlblcvjbljcvjb'


#form
class TestForm(FlaskForm):
    name=StringField('what is your name ',validators=[DataRequired()])
    number=IntegerField('numer')
    submit=SubmitField('submit')



#form handiling 


@app.route('/',methods=['GET','POST'])
def home():
    name=False
    num=False
    form=TestForm()
    if form.validate_on_submit():
        num=form.number.data
        name=form.name.data
        form.number.data=''
        form.name.data=''
        print (name)
        print (num)

    return render_template('index.html',name=name,form=form,num=num)



if __name__=='__main__':
    app.run(debug=True)