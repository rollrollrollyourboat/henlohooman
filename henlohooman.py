from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import logging

updater = Updater(token='780805165:AAEdreGeX_G1ECiU6dWo2cF9UHrk545agAw')

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text="Henlo hooman! Tell me how are you feeling today! 😌")

def isJoke(bot, update):
  getJoke = False
  if 'joke' in update.message.text:
    getJoke = True
  elif 'tell me' in update.message.text:
    getJoke = True
  elif 'funny' in update.message.text:
    getJoke = True
  elif 'sad' in update.message.text:
    getJoke = True
  elif 'cheer' in update.message.text:
    getJoke = True
  elif 'doge' in update.message.text:
    getJoke = True

  return getjoke

start_handler = CommandHandler('start', start)
joke_handler = MessageHandler(Filters.text, isJoke)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(joke_handler)


updater.start_polling()
