import random

class GifGiver():
  def __init__(self):
    with open('Gifs/gifs.txt', 'r') as f:
      self._gifs = f.readlines()

  def pollGif(self):
    return self._gifs[random.randint(0, len(self._jokes) - 1)];