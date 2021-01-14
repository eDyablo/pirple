class Player:
  def __init__(self):
    self.__hand = []

class Game:
  def __init__(self, pattern):
    self.__pattern = pattern
    self.__deck = None

  def play(self):
    self.__deck = self._build_deck()
    print(self.__deck)

  def _build_deck(self):
    deck = self.__pattern.build_deck()
    deck.shuffle()
    return deck
