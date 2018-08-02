from flask import flash, redirect, url_for, render_template
from flask_login import login_required, current_user
from wtforms import ValidationError
from flask import request, abort

from . import profile
from ..secret import secret
from .forms import ChangePasswordForm
from .. import db
from ..models import User
from wtforms import TextField

@profile.route('/profile', methods=['GET', 'POST'])
@login_required

def show_update_profile():
    form = ChangePasswordForm()
    form.username.data = current_user.username
    if request.method == 'POST':
        username = request.form.get('username')
        print(username)
        old_password = request.form.get('old_password')
        print(old_password)
        new_password = request.form.get('new_password')
        new_password_confirm = request.form.get('new_password_confirm')
        is_admin = request.form.get('is_admin')
        user = User.query.filter_by(username=username).first()
        print('before evaluation')
        if not user:
            print('usernot existant')
            return abort(404)
        if not user.verify_password(old_password):
            print('eval1')
            flash('Old password does not match your actual password')
            return redirect(url_for('profile.show_update_profile'))
        elif new_password == old_password:
            print('eval2')
            flash('New password should be different from old one')
            return redirect(url_for('profile.show_update_profile'))
        elif new_password != new_password_confirm:
            print('eval3')
            flash('New password and Confirmation do not match')
            return redirect(url_for('profile.show_update_profile'))
        elif is_admin == 'y':
            print('eval4')
            if not current_user.is_admin:
                flash('You are not allowed!... Only admins')
                print('not allowed')
                return redirect(url_for('profile.show_update_profile'))
        print('in here')
        user.password = new_password
        if is_admin == 'y':
            is_admin = 1
        else:
            is_admin = 0
        user.is_admin = is_admin
        print('before commit')
        db.session.add(user)
        db.session.commit()
        flash('You have successfully updated your profile!')
        return redirect(url_for('profile.show_update_profile'))
    """
    form = ChangePasswordForm()
    form.username.data=current_user.username
    print(type(form.username.data))
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user.verify_password(form.old_password.data):
            flash('Old password does not match your actual password')
        elif form.new_password.data == form.old_password.data:
            flash('New password should be different from old one')
        elif form.new_password.data != form.new_password_confirm.data:
            flash('New password and Confirmation do not match')
        elif not current_user.is_admin and form.is_admin.data == '1':
            flash('You are not allowed!... Only admins')
        else:
            user.password=form.new_password.data
            user.is_admin=form.is_admin.data
            db.session.add(user)
            db.session.commit()
            flash('You have successfully updated your profile!')
            return redirect(url_for('profile.show_update_profile'))
    """
    return render_template('profile/profile.html',form=form)
