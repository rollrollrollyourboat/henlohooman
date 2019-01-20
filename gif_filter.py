from telegram.ext import BaseFilter

class GifFilter(BaseFilter):
  def filter(self, message):
    if len(message.text) > 10:
      for word in ['gif', 'GIF']:
        if word in message.text.lower():
          return True