from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import BaseFilter

class JokeFilter(BaseFilter):
  def filter(self, message):
    if len(message.text) > 10 :
      for word in ['joke', 'tell me', 'funny', 'sad', 'cheer', 'doge']:
        if word in message.text.lower():
          return True
