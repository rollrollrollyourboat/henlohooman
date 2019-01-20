from telegram.ext import BaseFilter

class StickerFilter(BaseFilter): 
  def filter(self, message):
    if len(message.text) > 10 :
      for word in ['sticker']:
        if word in message.text.lower():
          return True

    return False
