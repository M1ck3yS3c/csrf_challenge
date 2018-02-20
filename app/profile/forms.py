from flask_wtf import FlaskForm
from flask_login import current_user
from  werkzeug.security import generate_password_hash
from wtforms import PasswordField, BooleanField, SelectField, SubmitField, ValidationError
from wtforms.validators import DataRequired, EqualTo

from ..models import User

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    new_password_confirm = PasswordField('Confirm New Password')
    is_admin = BooleanField('Admin', default=False)
    #is_admin = SelectField('Admin',choices=[(True,'Admin')])
    submit = SubmitField('Update')
