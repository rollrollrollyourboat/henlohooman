from telegram.ext import BaseFilter

class StickerFilter(BaseFilter): 
  def filter(self, message): 
    for word in ['sticker']:
      if word in message.text.lower():
        return True

    return False
