from telegram.ext import BaseFilter

class UnglamStickerFilter(BaseFilter): 
  def filter(self, message): 
    for word in ['unglam']:
      if word in message.text.lower():
        return True

    return False
