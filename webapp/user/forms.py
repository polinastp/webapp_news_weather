from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()],render_kw={"class": "form-control"})
    password = PasswordField('Password', validators = [DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Remember me', default=True, render_kw={'class':'form-check-input'}) #checkbox
    submit = SubmitField('Send', render_kw={"class":"btn btn-primary"})

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()],render_kw={"class": "form-control"})
    email = StringField('Email', validators = [DataRequired(), Email()], render_kw={"class": "form-control"} )
    password = PasswordField('Password', validators = [DataRequired()], render_kw={"class": "form-control"} )
    password2 = PasswordField('Repeat password', validators = [DataRequired(), EqualTo('password')], render_kw={"class": "form-control"} )
    submit = SubmitField('Send', render_kw={"class":"btn btn-primary"})