import random
import glob

class ImageGiver():
  def __init__(self):
    self._images = glob.glob('Images/*.*')

  def pollImage(self):
    return self._images[random.randint(0, len(self._images) - 1)]