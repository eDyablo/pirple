from playcard import (
  EnglishPattern,
)

from crazy_eights import Game

if __name__ == '__main__':
  game = Game(EnglishPattern())
  game.play()
