from os.path import (
    abspath,
    dirname,
    join as join_path,
)

'''
Art is a game art which is set of frames that get loaded from a text file.
Draws its current frame on a screen.
'''
class Art:
  def __init__(self):
    self.frames = []

  def load(self, art_file):
    frames = []
    frame_height = 0
    try:
      frame_height = int(art_file.readline())
      if frame_height <= 0:
        return
    except ValueError:
      return
    frame = []
    line_count = 0
    for line in art_file:
      frame.append(line.strip('\n\r'))
      line_count += 1
      if line_count % frame_height == 0:
        frames.append(frame)
        frame = []
    self.frames = frames

  def load_from_file(self, name):
    art_path = join_path(dirname(abspath(__file__)), join_path('arts', name))
    try:
      with open(art_path, 'r') as art_file:
        self.load_from_file(art_file)
    except FileNotFoundError:
      pass
