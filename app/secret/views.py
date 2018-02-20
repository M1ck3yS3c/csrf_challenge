from flask import render_template, url_for
from flask_login import login_required, current_user
from .import secret

@secret.route('/secret')
@login_required
def secret():
    if  current_user.is_admin != False:
        return render_template('secret/flag.html')
    return render_template('secret/nope.html')