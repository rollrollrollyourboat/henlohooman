import random

class SmallTalkSender():
  def __init__(self):
    self._smallTalk = [
   'hOOman i hope u want tis',
   'hemlo jusd came to say u bOOtifu',
   'Pupper request hug needs snug',
   'henlo fren i hope this give smiles',
   'Omgosh boop!',
   'am comf if hOOman luvs mi',
   'a day is never ruff if u get tis',
   'am requesting pat now',
   'hOOman would u want a pupcake',
   'wishes you a hapuppy day',
   'woterfol goes kssshhh',
   'puppo goes AwoOoOoO, hooman goes AchoOoOo',
   'doggo smells hotdoggo in hoOman tummy',
   'hooman smal, doggo am tol',
   'gib me immediate chimken nugge- NOW',
   'hey frendo, feeling heck? Do not worry!',
   'HENLO',
   'hehehehe, had too many chimken nuggers',
   'zoom zoom doggo on wheels is fast as hoOman'
    ];

  def pollSmallTalk(self):
    return self._smallTalk[random.randint(0, len(self._smallTalk) - 1)];