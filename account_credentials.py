class Credential:
    def __init__(self, web_site, user_name, user_password):
        self.web_site = web_site
        self.user_name = user_name
        self.user_password = user_password

    my_account = []

    def save_credential(self):
        """
        this is a method that appends the website 
        """
        Credential.my_account.append(self)

    def delete_account(self):
        """
        this is a method that deletes a selected account
        """
        Credential.my_account.remove(self)

    @classmethod
    def display_account(cls):
        """
        method that returns the credentials list
        """
        return cls.my_account

    @classmethod
    def find_by_website(cls, website):
        """
        method that takes in a website and returns a password credential that matches that credential

        Args:
            website: Website name to search for password credentials
         Returns:
            Password of person that matches the website
        """

        for credential in cls.my_account:
            if credential.web_site == website:
                return credential

    @classmethod
    def account_exists(cls, website):
        """
        method that checks if a password credential exists from the credentials list

        Args:
            website ([Boolean]): True or false depending if the credential exists
        """
        for credential in cls.my_account:
            if credential.web_site == website:
                return True
       
    @classmethod
    def display_credentials(cls):
        """
        method that returns the credentials list
        """
        return cls.my_account
