FROM python:3.6-stretch

LABEL maintainer "Mike Fotso <hmkf1993@gmail.com>"

RUN apt-get update && apt-get upgrade -y

RUN mkdir /ded_sec

WORKDIR /ded_sec

COPY . /ded_sec/

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=run.py
ENV FLASK_CONFIG=production

EXPOSE 5000

RUN apt-get install -y cron
#RUN echo "1 * * * * /ded_sec/app/bot/run_bot.sh >> /var/log/cron.log 2>&1" >> /etc/crontab
#COPY crontab_run_bot /etc/cron.d/crontab_run_bot
#RUN touch /var/log/cron.log
#RUN crontab -l ; echo "* * * * * echo "Hello world" >> /var/log/cron.log" | crontab
#RUN service cron start

#RUN apt-get install -y supervisor
#RUN apt-get install -y cron
#RUN mkdir -p /var/log/supervisor
#RUN cat ded_sec.conf >> /etc/supervisord.conf
#RUN service supervisor restart
#RUN cron
#CMD gunicorn run:app -b 0.0.0.0:5000
CMD [bootstrap.sh]
