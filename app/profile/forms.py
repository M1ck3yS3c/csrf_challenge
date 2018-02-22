from flask_wtf import FlaskForm
from flask_login import current_user
from  werkzeug.security import generate_password_hash
from wtforms import PasswordField, BooleanField, SubmitField,HiddenField
from wtforms.validators import DataRequired, EqualTo

from ..models import User

class ChangePasswordForm(FlaskForm):
    username = HiddenField('Username',default=current_user)
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    new_password_confirm = PasswordField('Confirm New Password')
    is_admin = BooleanField('Admin', default=False)
    submit = SubmitField('Update')
