import unittest
from password import Password
import pyperclip
import uuid

class TestPassword(unittest.TestCase):
    """
    Test class that defines test cases for the password class behaviours

    Args:
        unittest : TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run before each test cases
        """
        self.new_password = Password("Evernote", "John", "Osiko", "johnmaxosiko@gmail.com", "projecttest1")


    def test_init(self):
        """
        test__init test case to test if the my_password object is initialized properly
        """
        self.assertEqual(self.new_password.web_site, "Evernote")
        self.assertEqual(self.new_password.first_name, "John")
        self.assertEqual(self.new_password.last_name, "Osiko")
        self.assertEqual(self.new_password.user_name, "johnmaxosiko@gmail.com")
        self.assertEqual(self.new_password.user_password, "projecttest1")

    