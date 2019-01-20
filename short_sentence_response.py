from telegram.ext import BaseFilter

class ShortSentenceResponse(BaseFilter): 
  def filter(self, message): 
    if len(message.text) < 10 :
      return True

    return False
