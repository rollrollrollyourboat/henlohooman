import random

class UnglamStickerGiver():
  def __init__(self):
    with open('unglamsticker/unglamSticker.txt', 'r') as f:
      self._unglamStickers = f.readlines()

  def pollUnglamSticker(self):
    returnString = self._unglamStickers[random.randint(0, len(self._unglamStickers) - 1)]
    returnString = returnString[:-1]
    return returnString;