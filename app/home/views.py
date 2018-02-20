from flask import render_template
from flask_login import login_required

from . import home
#from ..bot import bot
#from apscheduler.schedulers.background import BackgroundScheduler

# scheduler
#scheduler = BackgroundScheduler()
#scheduler.start()
@home.route('/')
def homepage():
    return render_template('home/index.html', title='Welcome to DedSec Blog')

@home.route('/dashboard')
@login_required
def dashboard():
    #scheduler.add_job(bot.run_bot(), 'interval', minutes=5, id='running_bot')
    return render_template('home/dashboard.html', title='DedSec - Dashboard')