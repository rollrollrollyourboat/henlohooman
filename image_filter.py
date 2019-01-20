from telegram.ext import BaseFilter

class ImageFilter(BaseFilter): 
  def filter(self, message):
    if len(message.text) > 10:
      for word in ['image', 'pic', 'photo', 'piktares']:
        if word in message.text.lower():
          return True