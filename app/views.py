from app import app
from flask import render_template,redirect,url_for,flash
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/user/<username>')
def user(username):
	return render_template('user.html',name=username)

@app.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash(form.username.data)
		return redirect(url_for('index'))
	return render_template('login.html',form=form)
