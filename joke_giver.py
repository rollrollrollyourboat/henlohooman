import random

class JokeGiver():
  def __init__(self):
    with open('Jokes/jokes.txt', 'r') as f:
      self._jokes = f.read().split("\n--\n")

  def pollJoke(self):
    return self._jokes[random.randint(0, len(self._jokes) - 1)];