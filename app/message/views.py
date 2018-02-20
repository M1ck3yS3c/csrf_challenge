from flask import flash, redirect, url_for, render_template
from flask_login import login_required, current_user
import re
from .import message
from .forms import MessageForm
from .. import db
from ..models import Message


@message.route('/send_message', methods=['GET', 'POST'])
@login_required
def send_message():
    form = MessageForm()
    #c_user = str(current_user)
    #c_user = re.sub('[User:]', '', c_user)
    #c_user = re.sub('[<>]','',c_user)
    message_feed = []
    message_feed = Message.query.filter_by(author=current_user.username).all()
    if form.validate_on_submit():
        message = Message(title=form.title.data,
                          body=form.body.data,
                          author=current_user.username)
        db.session.add(message)
        db.session.commit()
        flash('Message sent successfully! We will get back to you')
        return redirect(url_for('message.send_message',form=form,message_feed=message_feed))

    return render_template('/message/send_message.html',form=form,message_feed=message_feed)