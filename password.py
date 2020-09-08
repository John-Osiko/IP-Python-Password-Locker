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

    