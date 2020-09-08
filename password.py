import pyperclip
import uuid
class Password:
    """
    Class that generates new instances of passwords
    """
    my_password = []

    def __init__(self, web_site, first_name, last_name, user_name, user_password):
        self.web_site = web_site
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.user_password = user_password

    def save_password(self):
    
        """
        save_password method saves password objects into my_password
        """

        Password.my_password.append(self)

    def delete_password(self):
        """
        delete_password method deletes a saved password
        """
        Password.my_password.remove(self)

    @classmethod
    def find_by_website(cls, website):
        """
        method that takes in a website and returns a password credential that matches that username

        Args:
            website: Website name to search for password credentials
         Returns:
            Password of person that matches the website
        """

        for password in cls.my_password:
            if password.web_site == website:
                return password
       
    