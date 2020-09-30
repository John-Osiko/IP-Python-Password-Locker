import unittest
from password import User
import pyperclip
import uuid

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the password class behaviours

    Args:
        unittest : TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run before each test cases
        """
        self.new_password = User("Evernote", "John", "Osiko", "johnmaxosiko@gmail.com", "projecttest1")


    def test_init(self):
        """
        test__init test case to test if the user_info object is initialized properly
        """
        self.assertEqual(self.new_password.web_site, "Evernote")
        self.assertEqual(self.new_password.first_name, "John")
        self.assertEqual(self.new_password.last_name, "Osiko")
        self.assertEqual(self.new_password.name, "johnmaxosiko@gmail.com")
        self.assertEqual(self.new_password.password, "projecttest1")

    def test_save_password(self):
        """
        test_save_password case to test if the password object is saved into the password list
        """
        self.new_password.save_password()
        self.assertEqual(len(User.user_info),1)

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run
        """
        User.user_info = []


    def test_save__multiple_password(self):
        """
        test_save_multiple_password to check if we can save multiple passwords to our user_info
        """
        self.new_password.save_password()
        test_password = User("Page", "name1", "name2", "username", "testuser")
        test_password.save_password()
        self.assertEqual(len(User.user_info),2)

    def test_password_exists(self):
        """
        test to check if we can return a Boolean if we cannot find the password
        """
        self.new_password.save_password()
        test_password = User("Page", "name1", "name2", "username", "testuser")
        test_password.save_password()

        password_exists = User.password_exists("username")

        self.assertTrue(password_exists)

    def test_display_all_passwords(self):
        """
        method that returns a list of all passwords saved
        """

        self.assertEqual(User.display_passwords(),User.user_info)

    def test_copy_username(self):
        """
        Test to confirm that we are copying the user password from a found password credential
        """

        self.new_password.save_password()
        User.copy_username("username")

        self.assertEqual(self.new_password.password,pyperclip.paste())


    def test_delete_password(self):
        """
        test_delete_password to test if we can remove a password from our password list
        """
        self.new_password.save_password()
        test_password = User("Page", "name1", "name2", "username", "testuser")
        test_password.save_password()
        self.new_password.delete_password()
        self.assertEqual(len(User.user_info),1)

    def test_get_user_into_by_username(self):
        """
        test to check if we can find a password credential by website and display in formation 
        """
        self.new_password.save_password()
        test_password = User("Page", "name1", "name2", "username", "testuser")
        test_password.save_password()
        password_found = User.find_by_password("testuser")
        self.assertEqual(password_found.password,test_password.password)


if __name__ == '__main__':
    unittest.main()
