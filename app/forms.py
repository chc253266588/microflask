from wtforms import StringField,  BooleanField, SubmitField
from wtforms.validators import Required
from flask_wtf import Form

class LoginForm(Form):
	username = StringField('username', validators=[Required()])
	remember_me = BooleanField('Keep me logged in', default=False)
	submit = SubmitField('Log In')
