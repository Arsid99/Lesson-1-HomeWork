from unittest import TestCase
from Lesson_16.Task_3 import *


class PasswordCheckTestCase(TestCase):

    def test_check_pass_positive_result(self):
        self.assertEqual(client_code(), 'The password is correct')

    def test_exceptions(self):
        self.assertEqual(client_code('Roma@@@@'), 'There must be at least one digit.')
        self.assertEqual(client_code('roma123@@@@'), 'There must be at least 1 uppercase letter.')
        self.assertEqual(client_code('ROMA123@@@@'), 'There must be at least 1 letter in lower case.')
        self.assertEqual(client_code('Roma1234567'), 'There must be at least 1 single character: @, #, $, -, +, =.')
        self.assertEqual(client_code('Roma@12'), 'The length of the password must be at least 8 characters.')
