from flask import flash, redirect, url_for, render_template
from flask_login import login_required, current_user
from wtforms import ValidationError

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
    form.username.data=current_user.username
    if form.validate_on_submit():
        if not current_user.verify_password(form.old_password.data):
            flash('Old password does not match your actual password')
        elif form.new_password.data == form.old_password.data:
            flash('New password should be different from old one')
        elif form.new_password.data != form.new_password_confirm.data:
            flash('New password and Confirmation do not match')
        elif not current_user.is_admin and form.is_admin.data == '1':
            flash('You are not allowed!... Only admins')
        else:
            user = User.query.get_or_404(current_user.id)
            user.password=form.new_password.data
            user.is_admin=form.is_admin.data
            db.session.add(user)
            db.session.commit()
            flash('You have successfully updated your profile!')
            return redirect(url_for('profile.show_update_profile'))
    return render_template('profile/profile.html',form=form)
