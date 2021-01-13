from random import shuffle

class Suite:
  def __init__(self, name, symbol):
    self.name = name
    self.symbol = symbol

  def __str__(self):
    return self.symbol

class Card:
  def __init__(self, suite, face, score, symbol=''):
    self.face = face
    self.score = score
    self.suite = suite

  def __str__(self):
    return str(self.suite) + str(self.face)

class Deck:
  def __init__(self, suites, faces):
    self.cards = []
    for suite in suites:
      for face in faces:
        self.cards.append(Card(suite, face, 0))

  def __str__(self):
    return ' '.join(map(str, self.cards))

  def shuffle(self):
    shuffle(self.cards)

class Player:
  def __init__(self, name, money = 0, hand = []):
    self.hand = hand
    self.money = money
    self.name = name
    self.setScore()

  def __str__(self):
    records = [
      self.name,
      ' '.join(map(str, self.hand)),
      self.score,
    ]
    return ' '.join(map(str, records))

  def setScore(self):
    self.score = sum(map(lambda card: card.score, self.hand))

class Game:
  def __init__(self):
    self.suites = [
      Suite('hearts', '♥'),
      Suite('spades', '♠'),
      Suite('clubs', '♣'),
      Suite('diamands', '♦'),
    ]
    self.faces = list(map(str, range(2, 11))) + ['A', 'J', 'K', 'Q']

  def play(self):
    deck = Deck(self.suites, self.faces)
    deck.shuffle()
    print(deck)
    player = Player('Ed', 100, [Card(Suite('spades', '♠'), 'A', 10)])
    print(player)
