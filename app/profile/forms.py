from flask_wtf import FlaskForm
from  werkzeug.security import generate_password_hash
from wtforms import PasswordField, BooleanField, SubmitField, HiddenField, TextField
from wtforms.validators import DataRequired, EqualTo

from ..models import User
class ChangePasswordForm(FlaskForm):
    username = HiddenField('Username')
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    new_password_confirm = PasswordField('Confirm New Password', validators=[DataRequired()])
    is_admin = BooleanField('Admin', default=False)
    submit = SubmitField('Update')
