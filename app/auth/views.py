from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import User


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash('Username already exist please choose another one!')
        else:
            user = User(username=form.username.data,
                        password=form.password.data)
            db.session.add(user)
            db.session.commit()
        flash('You have successfully registered! You may login.')

        #redirect to login page
        return redirect(url_for('auth.login'))

    #load registration template
    return render_template('auth/register.html', form=form, title='Register')

@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(
            form.password.data
        ):
            login_user(user)
            return redirect(url_for('home.dashboard'))

        else:
            flash('Invalid Username or Password')
    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    #handling logout request
    flash('You are being logged out.')

    #redirect to login page
    return redirect(url_for('auth.login'))




