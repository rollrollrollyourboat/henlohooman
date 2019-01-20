from telegram.ext import BaseFilter

class UnglamStickerFilter(BaseFilter): 
  def filter(self, message):
    if len(message.text) > 10 :
      for word in ['unglam']:
        if word in message.text.lower():
          return True

    return False
