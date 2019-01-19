import random

class StickerGiver():
  def __init__(self):
    with open('stickers/stickers.txt', 'r') as f:
      self._stickers = f.readlines()

  def pollSticker(self):
    returnString = self._stickers[random.randint(0, len(self._stickers) - 1)]
    returnString = returnString[:-1]
    return returnString;