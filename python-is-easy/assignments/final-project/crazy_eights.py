from playcard import Deck


class Player:
    def __init__(self, name):
        self.__hand = Deck()
        self.__name = name

    def __str__(self):
        return ' '.join(map(str, [
            'player',
            self.__hand,
        ]))

    def buy(self, stock):
        self.__hand.put(stock.draw())

    def get_hand(self):
        return self.__hand.copy()


class Game:
    def __init__(self, pattern, players):
        self.__deck = None
        self.__discardpile = Deck()
        self.__pattern = pattern
        self.__players = players

    def play(self):
        self.build_deck()
        self.deal_cards()
        print(self.__deck)
        print(self.__discardpile)
        for index, card in self.__players[0].get_hand().enumerate():
            print(index + 1, card)

    def build_deck(self):
        deck = self.__pattern.build_deck()
        deck.shuffle()
        self.__deck = deck

    def deal_cards(self):
        for i in range(0, 5):
            for player in self.__players:
                player.buy(self.__deck)
        self.__discardpile.put(self.__deck.draw())
