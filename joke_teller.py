import random

class JokeTeller():
  def __init__(self):
    self._jokes = [
    'Q: What do you get when you cross a dinosaur with a pig?\n\nA: Jurrassic Pork.',
    'Q: Why didn\'t the elephant like to play cards in the jungle?\n\nA: A: Because there were too many cheetahs.'
    ];

  def pollJoke(self):
    return self._jokes[random.randint(0, len(self._jokes) - 1)];