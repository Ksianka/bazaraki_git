from __future__ import absolute_import, unicode_literals
from bazaraki_parser import bazaraki_parser
import telebot
import redis
import os
token = '' # Input your Telegram bot token here as str
bot = telebot.TeleBot(token)
import datetime

header = {'Accept': '*/*', 'User-Agent':
          ''}  # Input your User-Agent details as str. Can be found through your web browser inspector mode.
base_url = ''  # Inout your Bazaraki web link with proper search filters as str.

r = redis.from_url(os.environ.get("REDIS_URL"))  # Redis for Heroku enviroment
# r = redis.StrictRedis(host='localhost', port=6379, db=0)  # you can test on your localhost, in this case comment the string above and use this one


from telegram.ext import Updater, CommandHandler


def start(bot, update):
    adverts = bazaraki_parser(base_url, header)
    keys = r.keys()
    sent_count = 0
    for ad in adverts:
        if bytes(adverts[ad], 'utf-8') not in keys:
            bot.send_message(chat_id='', text=str(adverts[ad]))  # Input your Telegram Channel name in chat_id as str
            sent_count += 1
            r.set(adverts[ad], str(datetime.datetime.now()))


u = Updater(token=token)

j = u.job_queue
j.run_repeating(start, interval=7200, first=0)   # Current bot start interval -  2hours or 7200 seconds.

u.start_polling()
u.idle()
