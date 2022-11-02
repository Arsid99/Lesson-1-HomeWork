from unittest import TestCase
from Lesson_16.Task_2 import PhoneNumber


class PhoneNumberTestCase(TestCase):
    def setUp(self):
        self.phone = '+380-68-995-15-35'

    def test_phone_number_check(self):
        self.assertRegex(PhoneNumber(self.phone).format_ua_num(),
                         r"\(\+\d\d\) \d{3} \d{3}-\d{2}-\d{2}")

    def test_phone_negative(self):
        self.assertNotRegex(PhoneNumber('+380-68-995-15').format_ua_num(),
                            r"\(\+\d\d\) \d{3} \d{3}-\d{2}-\d{2}")
        self.assertNotEqual(PhoneNumber('+30689951').format_ua_num(), '(+30) 689 951')
        self.assertNotEqual(PhoneNumber('+30689951').format_ua_num(), '(+38) 306 899-51')

    def test_phone_type(self):
        self.assertIsInstance(PhoneNumber(self.phone).format_ua_num(), str)

    def tearDown(self):
        del self.phone