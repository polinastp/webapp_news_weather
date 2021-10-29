from flask import Blueprint, blueprints, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

from webapp.db import db
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User

blueprint = Blueprint('user', __name__, url_prefix='/users')

@blueprint.route('/login')
def login():
        if current_user.is_authenticated:
            return redirect(url_for('news.index'))
        title = "Sign in"
        login_form = LoginForm()
        return render_template('user/login.html', page_title=title, form=login_form)

@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('You are successfully loged in')
            return redirect(url_for('news.index'))

    flash('Invalid username or password')
    return redirect(url_for('user.login'))

@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    title = "Registration"
    form = RegistrationForm()
    return render_template('user/registration.html', page_title=title, form=form)

@blueprint.route('/logout')
def logout():
    logout_user()
    flash('You are successfully loged out')
    return redirect(url_for('news.index'))

@blueprint.route('/precess-reg', methods=['POST'])
def process_reg():
    form=RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('You are successfully a user now')
        return redirect(url_for('user.login'))
    flash('Something is wrong in a form')
    return redirect(url_for('user.register'))