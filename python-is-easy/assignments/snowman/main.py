from os import (
    name as os_name,
    system as system_call,
)

from os.path import (
    abspath,
    dirname,
    join as join_path,
)

class Screen:
    def clear(self):
        if os_name == 'nt':
            system_call('cls')
        else:
            system_call('clear')

    def draw(self, frame):
        for line in frame:
            print(line, end='')

class Input:
    def ask(self, message):
        answer = ''
        while answer == '':
            answer = input(message)
        return answer

class Art:
    def __init__(self):
        self.frames = []
        self.current_frame = 0

    def load(self, name):
        frames = []
        art_path = join_path(dirname(abspath(__file__)), join_path('arts', name))
        with open(art_path, 'r') as art_file:
            frame_height = int(art_file.readline())
            frame = []
            line_count = 0
            for line in art_file:
                frame.append(line)
                line_count += 1
                if line_count % frame_height == 0:
                    frames.append(frame)
                    frame = []
        self.frames = frames
        self.current_frame = 0

    def draw(self, screen):
        screen.draw(self.frames[self.current_frame])

    def next_frame(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)

class Riddle:
    def __init__(self, key):
        self.key = key
        self.clue = ['_'] * len(key)

    def length(self):
        return len(self.key)

    def range(self):
        return range(0, self.length())

    def guess(self, g):
        guess_count = 0
        for i in self.range():
            if g == self.key[i]:
                guess_count += 1
                self.clue[i] = g
        return guess_count

    def solved(self):
        for i in self.range():
            if self.clue[i] != self.key[i]:
                return False
        return True

    def unsolved(self):
        return self.solved() == False

    def draw(self, screen):
        screen.draw([' '.join(self.clue), '\n'])

class Game:
    def __init__(self):
        self.screen = Screen()
        self.input = Input()
        self.art = Art()
        self.riddle = Riddle('riddle')

    def play(self):
        self.art.load('snowman')
        self.propose_riddle()
        while self.in_progress():
            self.play_round()
        self.end()

    def propose_riddle(self):
        self.riddle = Riddle(self.input.ask('Player 1 pick a word: '))

    def in_progress(self):
        return self.riddle.unsolved()

    def draw_frame(self):
        self.screen.clear()
        self.art.draw(self.screen)
        self.riddle.draw(self.screen)

    def play_round(self):
        self.draw_frame()
        clue = input('Player 2 guess a letter: ')
        if len(clue) > 0:
            if self.riddle.guess(clue[0]) == 0:
                self.art.next_frame()

    def end(self):
        self.draw_frame()

game = Game()
game.play()
