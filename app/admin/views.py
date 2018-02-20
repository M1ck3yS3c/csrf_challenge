from . import admin
from flask import flash, redirect, url_for, render_template
from flask_login import login_required, current_user
from app import message
from .. import db
from ..models import Message

@admin.route('/unread_messages')
def read_messages():
        unread_messages_string = []
        unread_messages = Message.query.filter_by(response=None).all()
        for i in range(len(unread_messages)):
            #print(type(unread_messages[i]))
            unread_messages_string.append(unread_messages[i].body)
            unread_messages[i].response = "Message recieved.. We will get back to you soon"
            db.session.add(unread_messages[i])
            db.session.commit()
            #print(unread_messages)
            #flash('Message sent successfully! We will get back to you')
        return render_template('admin/unread_messages.html', unread_messages=unread_messages_string)

