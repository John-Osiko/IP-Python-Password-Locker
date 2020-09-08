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


    