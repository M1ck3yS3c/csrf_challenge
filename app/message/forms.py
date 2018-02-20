from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

from ..models import Message

class MessageForm(FlaskForm):
    #Form to send a message to admin
    title = StringField('Subject', validators=[DataRequired()])
    body = TextAreaField('Body')
    submit = SubmitField('Send')

    def validate_message(self,title):
        if not title:
            raise ValidationError('Please add a Subject!')
