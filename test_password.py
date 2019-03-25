from unittest import TestCase
from Password import Password

class TestPassword(TestCase):
    def test_check(self):
        pwd = Password("avc")
        self.assertEqual(True, pwd.check("avc"))

    def test_check1(self):
        pwd = Password("asd")
        self.assertEqual(True, pwd.check("asd"))

    def test_check3(self):
        pwd = Password("asd")
        self.assertEqual(True, pwd.check("asd"))
