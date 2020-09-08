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

    def test_save_password(self):
        """
        test_save_password case to test if the password object is saved into the password list
        """
        self.new_password.save_password()
        self.assertEqual(len(Password.my_password),1)

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run
        """
        Password.my_password = []


    def test_save__multiple_password(self):
        """
        test_save_multiple_password to check if we can save multiple passwords to our my_password
        """
        self.new_password.save_password()
        test_password = Password("Page", "name1", "name2", "username", "testuser")
        test_password.save_password()
        self.assertEqual(len(Password.my_password),2)

    def test_password_exists(self):
        """
        test to check if we can return a Boolean if we cannot find the password
        """
        self.new_password.save_password()
        test_password = Password("Page", "name1", "name2", "username", "testuser")
        test_password.save_password()

        password_exists = Password.password_exists("username")

        self.assertTrue(password_exists)

    