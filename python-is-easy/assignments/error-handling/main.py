from io import StringIO
from unittest import (
  main as run_tests,
  TestCase,
)

from snowman import Art

class ArtTest(TestCase):
  def setUp(self):
    self.art = Art()

  def test_load_from_non_existent_file_gives_empty_art(self):
    self.art.load_from_file('non-existent')
    self.assertEqual(self.art.frames, [])

  def test_load_empty_gives_empty_art(self):
    self.art.load(StringIO(''))
    self.assertEqual(self.art.frames, [])

  def test_load_single_frame(self):
    self.art.load(StringIO('1\nsingle frame'))
    self.assertEqual(self.art.frames, [['single frame']])

  def test_load_invalid_frame_height_definition_gives_empty_art(self):
    self.art.load(StringIO('height'))
    self.assertEqual(self.art.frames, [])

  def test_load_zero_frame_height_and_no_frames_gives_empty_art(self):
    self.art.load(StringIO('0'))
    self.assertEqual(self.art.frames, [])

  def test_load_one_frame_and_zero_frame_height_gives_empty_art(self):
    self.art.load(StringIO('0\nframe'))
    self.assertEqual(self.art.frames, [])

  def test_load_one_frame_and_negative_frame_height_gives_empty_art(self):
    self.art.load(StringIO('-1\nframe\nframe'))
    self.assertEqual(self.art.frames, [])

  def test_load_single_frame_having_two_lines_gives_valid_art(self):
    self.art.load(StringIO('2\nfirst\nsecond'))
    self.assertEqual(self.art.frames, [['first', 'second']])

  def test_load_two_single_line_frames_gives_valid_art(self):
    self.art.load(StringIO('1\nfirst\nsecond'))
    self.assertEqual(self.art.frames, [['first'], ['second']])

  def test_load_two_frames_gives_valid_art(self):
    self.art.load(StringIO('2\nfirst\nsecond\nfirst\nsecond'))
    self.assertEqual(self.art.frames, [['first', 'second'], ['first', 'second']])

if __name__ == '__main__':
  run_tests()
