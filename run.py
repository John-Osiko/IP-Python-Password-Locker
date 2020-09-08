#!usr/bin/env python3.6
from password import Password
from account_credentials import Credential
import uuid


def new_user_account():
    print('Create New user account')
    first_name = input('Enter First Name:.... ')
    last_name = input('Enter Last Name:.... ')
    user_name = input('Enter Username:.... ')

    if(User.password_exists(user_name)):
        print('User already exists')
        new_password()
    else:
        user_password = input('Type your login password: ')
        user_password1 = input('Confirm your login password: ')
        if user_password == user_password1:
            new_password = User(first_name, last_name,
                            user_name, usr_password)
            User.save_user_info(new_User)
            print(f'{first_name} added as user\n---------')
            login_account()


def login_account():
    print("-------Login-------")
    exists = User.user_login(input('Enter Username: '),
                             input('Enter Password: '))

    if(exists != True):
        print('Check your password!')
    else:
        acc_short_code = input('Hello, if you want to add an existing platform acccount, type px. If you want to generate new account details, type nw').lower()
        if(acc_short_code == 'nw'):
            reg_new_platform()
        elif acc_short_code == 'px':
            reg_existing_platform()
        else:
            print('Invalid Option. I did not really get that.')
            login_account()


def reg_existing_platform():
    px_platform = input('Enter platform e.g. Evernote, Facebook, Google, Instagram etc.: ')
    px_username = input('Enter account username/email: ')

    if(userAccounts.account_exist(px_platform, px_username)):
        print(
            'Account on {px_platform} already registered with username/email {px_username}')
    else:
        ex_password = input('Enter account password: ')
        new_password = userAccounts(
            px_platform, px_username, px_password)
        # Adding new account if it doesnt exist
        userAccounts.add_account(new_password)
        print(
            f'Account {px_username} added to platform {px_platform}')


def reg_new_platform():
    nw_platform = input('Enter platform e.g. Evernote, Facebook, Google, Instagram etc.: ')
    nw_username = input('Enter account username/email: ')
    nw_password = input('Type password or type AUTO to auto-generate password: ')

    if(nw_password == 'auto' or nw_password == 'AUTO'):
        nw_password = userAccounts.test_password(
            int(input('Enter preferred length: ')))
        print(f'Your password is {nw_password}')
    else:
        if(input('Confirm your password: ') != nw_password):
            print('Passwords didn\'t match')
            main()
    new_password = userAccounts(
        nw_platform, nw_username, nw_password)
    userAccounts.add_account(new_account)
    print(f'Account {nw_username} added to platform {nw_platform}')
    if input('Type cp to copy password').lower() == 'cp':
        pyperclip.copy(nw_password)
        print(f'Password of {nw_username } copied to clipboard')
        if input('Type LS to list all your credentials or press any key to return to main').lower() == 'ls':
            userAccounts.display_passwords()
        else:
            login_account()
    reg_new_platform()

def main():
    print("Hello! Welcome to your password locker\nUse cn to create an new user account, or lg to login to an existing user account")
    user_name = input()

    print(f"Hello {user_name}. What would you like to do?")
    print ('\n')

    while True:
                print("Use these short codes : cn - create a new password, dp - display passwords, fp - find a password, ex - exit the password list")
                short_code = input().lower()

                if short_code == 'cn':
                    new_user_account()

                    save_passwords(create_password(wsite, fname, lname, uname, upassword))
                    print ('\n')
                    print(f"New Password {first_name} {last_name} created")
                    print ('\n')

                elif short_code == 'dp':
                    if display_passwords():
                        print("Here is a list of all your passwords")

                        print ('\n')

                        for password in display_passwords():
                            print(f"{password.first_name} {password.last_name} ......{contact.user_name}")

                            print('\n')

                    else:
                            print('\n')
                            print("You do not seem to have any accounts saved yet")
                            print('\n')

                elif short_code == 'lg':
                    login_account()
                

                elif short_code == 'fp':

                            print("Enter the username you want to search for")

                            search_website = input()
                            if check_existing_passwords(search_website):
                                    search_website = find_password(search_website)

                                    print(f"{search_password.first_name} {search_password.last_name}")

                                    print('-' * 20)

                                    print(f"Username ........{search_password.user_name}")

                                    print(f"Password ........{search_password.password}")

                            else:
                                print("That password does not exist")

                elif short_code == "ex":
                                        print("Bye.......")
                                        break
                else:
                    print("Invalid option. I really didn't get that. Please use the short codes")
                                    
                                    
if __name__ = '__main__':
    main()