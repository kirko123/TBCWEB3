from flask import render_template, redirect, flash
from flask_login import login_user, logout_user, current_user, login_required   

from forms import RegisterForm, SearchForm, EditUserForm, LoginForm, EditSearchForm, AnswerForm
from ext import app, db
from models import Info, User, Question, Answer








@app.route("/", methods=["GET","POST"])
def index():
 info = Info.query.all()
 form = SearchForm()
 if form.validate_on_submit():
  existing_question = Question.query.filter(Question.question == form.language.data).first()
  if  existing_question :
   return redirect("/search")
  else:
   new_question = Question(question=form.language.data)
   db.session.add(new_question)
   db.session.commit()
   return redirect("/search")

 return render_template("index.html", info=info, form=form)

@app.route("/search", methods=["GET","POST"])
def search():
 search = Question.query.all()
 answer = Answer.query.all()
 form = AnswerForm()
 if form.validate_on_submit():
  new_answer = Answer(answer=form.answer.data)
  db.session.add(new_answer)
  db.session.commit()
  
 
 return render_template("search.html", search=search, form=form, answer=answer)


@app.route("/edit_search/<int:search_id>", methods=["GET","POST"])
def edit_search(search_id):
 search = Question.query.get(search_id)
 form = EditSearchForm(language = search.question)
 if form.validate_on_submit():
  search.question = form.language.data

  db.session.commit()
  return redirect("/search")
 
 return render_template("edit_search.html", form=form)

@app.route("/delete_search/<int:search_id>")
def delete_search(search_id):
 search = Question.query.get(search_id)

 db.session.delete(search)
 db.session.commit()

 return redirect("/search")

@app.route("/new1", methods=["GET", "POST"])
def index1():
 if current_user.is_authenticated:
  return redirect("/")    
 form = LoginForm()
 if form.validate_on_submit():
  user = User.query.filter(User.username == form.username.data).first()
  if user and user.check_password(form.password.data):
    login_user(user)
    return redirect("/")   
 return render_template("Login.html", form=form)

@app.route("/new2", methods=["GET","POST"]) 
def register():
 form = RegisterForm()
 if form.validate_on_submit():
  existing_user = User.query.filter(User.username == form.username.data).first()
  if  existing_user:
   flash('this username is already used try a diffrent one')
  else:
   new_user = User(username=form.username.data, password=form.password.data, birthday=form.birthday.data)
   flash('You were successfully Registerd')

   db.session.add(new_user)
   db.session.commit()
   return redirect("/")
  
 
 print(form.errors)
 return render_template("Register.html", form=form)

@app.route("/edit_user/<int:user_id>", methods=["GET","POST"])
def edit_user(user_id):
 user = User.query.get(user_id)
 form = EditUserForm(username=user.username, password=user.password, birthday=user.birthday)
 if form.validate_on_submit():
  user.username = form.username.data
  user.password = form.password.data
  user.birthday = form.birthday.data

  db.session.commit()
  return redirect("/registered_users")
  
 return render_template("edit_user.html", form=form)

@app.route("/registered_users")
def user():
 registered_users = User.query.all()
 return render_template("user.html", registered_users=registered_users)

@app.route("/delete_user/<int:user_id>")
def delete_user(user_id):
 user= User.query.get(user_id)

 db.session.delete(user)
 db.session.commit()

 return redirect("/registered_users")

@app.route("/logout")
def logout():
 logout_user()
 return redirect("/")

@app.route("/info/<int:info_id>")
@login_required
def index5(info_id):
 info = Info.query.get(info_id)
 return render_template("index5.html", inff=info)