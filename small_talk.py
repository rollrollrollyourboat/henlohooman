import random

class SmallTalkSender():
  def __init__(self):
    with open('smallTalk/smallTalk.txt', 'r') as f:
      self._smallTalk = f.readlines();

  def pollSmallTalk(self):
    return self._smallTalk[random.randint(0, len(self._smallTalk) - 1)];

  def setMood(self, moodlet):
    with open('smallTalk/' + moodlet + '.txt', 'r') as f:
      self._smallTalk += f.readlines();