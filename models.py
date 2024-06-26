from ext import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Info(db.Model):

    __tablename__ = "infos"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    inf = db.Column(db.String())
    moreinfo = db.Column(db.String())


    def __init__(self, name, inf, moreinfo):
        self.name = name
        self.inf = inf
        self.moreinfo = moreinfo
        

class Question(db.Model):

    __tablename__ = "post"

    id = db.Column(db.Integer(), primary_key=True)
    question = db.Column(db.String())


    def __init__(self, question):
        self.question = question

class Answer(db.Model):

    __tablename__ = "Answers"

    id = db.Column(db.Integer(), primary_key=True) 
    answer = db.Column(db.String())

    def __init__(self, answer):
        self.answer = answer  


  
   

class User(db.Model, UserMixin):    

    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    birthday = db.Column(db.Date())
    role = db.Column(db.String())

    def __init__(self, username, password, birthday, role="Guest"): 
        self.username = username
        self.password = generate_password_hash(password)
        self.birthday = birthday
        self.role = role
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)