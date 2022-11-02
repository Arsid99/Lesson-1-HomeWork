from unittest import TestCase
from Lesson_8.Task_2 import *


class ACDCTestLength(TestCase):

    def test_format(self):
        self.assertRegex(convert_to_preferred_format(duration_track(data)), r'[\d]{2}:[\d]{2}:[\d]{2}')

    def test_negative(self):
        self.assertNotEqual(convert_to_preferred_format(duration_track(data)), '00:00:00')
        self.assertNotEqual(convert_to_preferred_format(duration_track(data)), None)
