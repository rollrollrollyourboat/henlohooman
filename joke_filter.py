from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import BaseFilter

class JokeFilter(BaseFilter):
  def filter(self, message):
    getJoke = False

    if 'joke' in message.text:
      getJoke = True
    elif 'tell me' in message.text:
      getJoke = True
    elif 'funny' in message.text:
      getJoke = True
    elif 'sad' in message.text:
      getJoke = True
    elif 'cheer' in message.text:
      getJoke = True
    elif 'doge' in message.text:
      getJoke = True

    return getJoke