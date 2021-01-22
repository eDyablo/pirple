#!/usr/bin/env python3

from playcard import (
  EnglishPattern,
)

from crazy_eights import (
  Game,
  Player,
)

if __name__ == '__main__':
  game = Game(EnglishPattern(), [Player('first'), Player('second')])
  game.play()
