FROM python:3.6-stretch

LABEL maintainer "Mike Fotso <hmkf1993@gmail.com>"

RUN apt-get update && apt-get upgrade -y

RUN mkdir /ded_sec

WORKDIR /ded_sec

COPY . /ded_sec/

#MAKE ENTRYPOINT EXECUTABLE
RUN chmod +x bootstrap.sh

#INSALL REQUIREMENTS
RUN pip install --no-cache-dir -r requirements.txt

#SET ENVIRONEMENTAL VARIABLES
ENV FLASK_APP=run.py
ENV FLASK_CONFIG=production

#EXPOSE PORT 5000
EXPOSE 5000

#INSTALL CRON AND PHANTOMJS
RUN apt-get install -y cron
RUN apt-get install -y build-essential chrpath libssl-dev libxft-dev
RUN apt-get install libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /usr/local/share/
RUN ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin
RUN phantomjs --version
RUN crontab -l ;  echo "5 * * * * /ded_sec/app/bot/run_bot.sh >> /var/log/cron.log"  | crontab

#SET ENTRYPOINT
WORKDIR /ded_sec/
ENTRYPOINT ["./bootstrap.sh"]
