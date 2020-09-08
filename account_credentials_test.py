import unittest
import uuid
from account_credentials import Credential

class TestCredential(unittest.TestCase):
    """
    test class that defines the tets cases for the credential class behaviours

    Args:
        unittest : TestCase class helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run before each test cases
        """
        self.new_credential = Credential("Evernote","Clipper", "projecttest1")


    def test_init(self):
        """
        test_init test case is to test if the my_account object is initialized properly
        """
        self.assertEqual(self.new_credential.web_site, "Evernote")
        self.assertEqual(self.new_credential.user_name, "Clipper")
        self.assertEqual(self.new_credential.user_password, "projecttest1")


    def test_save_credential(self):
        """
        test_save_credential case is to test if the credential object is saved into our credentials list
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.my_account), 1)

    def test_delete_account(self):
        """
        test_delete case is to test if we can remove an account from our credentials list
        """
        self.new_credential.save_credential()
        test_credential = Credential("Facebook","Dripper Clipper", "testproject2")
        test_credential.save_credential()
        self.new_credential.delete_account()
        self.assertEqual(len(Credential.my_account), 1)

    def test_display_account(self):
        """
        method that returns a list of all passwords saved
        """

        self.assertEqual(Credential.display_account(), Credential.my_account)

    def test_find_password_credentials_by_website(self):
        """
        test to check if we can find a password credential by website and display in formation 
        """
        self.new_credential.save_credential()
        test_credential = Credential("Facebook", "Dripper Clipper", "testproject2")
        test_credential.save_credential()
        account_found = Credential.find_by_website("website")
        self.assertEqual(account_found.web_site, test_credential.user_password)

    def test_account_exists(self):
        """
        test to check if we can return a Boolean if we cannot find the password
        """
        self.new_credential.save_credential()
        test_credential = Credential("Facebook", "Dripper Clipper", "testproject2")
        test_credential.save_credential()

        account_exists = Credential.account_exists("username")

        self.assertTrue(account_exists)


    def test_display_all_credentials(self):
        """
        method that returns a list of all contacts saved
        """

        self.assertEqual(Credential.display_credentials(), Credential.my_account)



