from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, EmailField, DateField, RadioField, SubmitField

from wtforms.validators import DataRequired, Length, EqualTo

class RegisterForm(FlaskForm):
    email = EmailField("sheiyvanet emaili", validators=[DataRequired()])
    birthday = DateField("dabadebis tariri", validators=[DataRequired()])
    gender = RadioField("mornishnet sqwsi", choices=["kaci","qali"], validators=[DataRequired()])
    username = StringField("sheiyvane uzername", validators=[DataRequired()])
    password = PasswordField("chawere paroli", validators=[DataRequired(), Length(min=8, max=64,message="Too short")])
    repeat_password = PasswordField("gaiomeoret paroli", validators=[DataRequired(), EqualTo('password', 'Password mismatch')])   
    register = SubmitField("registracia")

class LoginForm(FlaskForm):
    username = StringField("sheiyvanet username")
    password = PasswordField("sheyvanet password")
    login =SubmitField("login")  

class SearchForm(FlaskForm):
    language = StringField("ask a question")
    find = SubmitField("post")

class AnswerForm(FlaskForm):
    answer = StringField("Answer")
    post = SubmitField("post")

class EditSearchForm(FlaskForm):
    language = StringField("change")
    save = SubmitField("post")    


class EditUserForm(FlaskForm):
    username = StringField("saxeli")
    password = PasswordField("paroli")
    birtday = DateField("dabadebis tariri")
    save =SubmitField("cvlilebebi shenaxava")