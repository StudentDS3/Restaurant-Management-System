import sys
sys.path.append('C:/Users/User/Documents/Restaurant-Management-System/src')
sys.path.append('C:/Users/User/Documents/Restaurant-Management-System/src/main/python')
import re
import os
from booking_users import User
from booking_errors import InvalidUserException, InvalidPasswordException, InvalidEmailException, \
    InvalidTypeException
import constants

directory = os.path.dirname(__file__)
user_db_path = os.path.join(directory, 'C:/Users/User/Documents/RMS/src/database/UserData.txt')


class Login:

    def __init__(self, uname, passwd):
        self.username = uname
        self.password = passwd

    def user_condition(self, uname, passwd):
        return True if uname == self.username and passwd == self.password else False

    def login(self):
        access_type = self.check_user()
        user = User(self.username, access_type)
        if access_type.upper() == 'ADMIN':
            print(f" {self.username}  Successfully logged In as {access_type}!!\n")
            user.admin_actions()
        elif access_type.upper() == 'STAFF' or access_type.upper() == 'STUDENT':
            print(f" {self.username}  Successfully logged In as {access_type} !!\n")
            user.student_staff_actions()
        else:
            print(f"login failed for {self.username} \n")
            exit()

    def check_user(self):
        with open(user_db_path, "r") as f:
            content = f.read().splitlines()
            for line in content:
                if len(line) != 0:
                    words = line.split(",")
                    user_username_pass_check = self.user_condition
                    if user_username_pass_check(words[0], words[1]):
                        return words[3]
        return "None"


class Register:
    def __init__(self, uname, passwd, mail, type_of_user):
        self.username = uname
        self.password = passwd
        self.email = mail
        self.type = type_of_user

    def register_user(self):
        with open(user_db_path, "a") as f:
            f.write("\n")
            caps_username, caps_type = map(lambda x: x.upper(), [self.username, self.type])
            f.write(caps_username + "," + self.password + "," + self.email + "," + caps_type)
            print(f" {self.username} Successfully registered in as {self.type}!!! ")


valid_user_check = lambda uname: True if re.match("^[a-zA-Z0-9_]+$", uname) else False

valid_password_check = lambda passwd: True if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', passwd) else False

valid_email_check = lambda mail: True if re.search(r'[\w.-]+@[\w.-]+.\w+', mail) else False

valid_usertype_check = lambda type_of_user: True if any(
    word in type_of_user for word in ['Student', 'Staff', 'Admin']) else False


def validate_user(reg_func_user_check, u_name):
    try:
        if not reg_func_user_check(u_name):
            raise InvalidUserException("Invalid user")
    except InvalidUserException:
        print(f"You entered invalid username {str(u_name)}")
        exit()


def validate_password(reg_func_password_check, password):
    try:
        if not reg_func_password_check(password):
            raise InvalidPasswordException("Invalid password")
    except InvalidPasswordException:
        print(f"You entered invalid password {str(password)} and it should contain at least 8 chars")
        exit()


def validate_email(reg_func_email_check, email):
    try:
        if not reg_func_email_check(email):
            raise InvalidEmailException("Invalid email")
    except InvalidEmailException:
        print(f"You entered invalid email format {str(email)}")
        exit()


def validate_type(reg_func_user_type_check, user_ty):
    try:
        if not reg_func_user_type_check(user_ty):
            raise InvalidTypeException("Invalid usertype")
    except InvalidTypeException:
        print(f"Please enter valid user type {str(user_ty)}")
        exit()


def actions():
    while True:
        print("------------------------------------------------------------------\n")
        print("            Welcome to the University  Restaurant   ")
        print("-------------------------------------------------------------------\n")
        print("""                 ====== Restaurant MENU=======
                                                 1. Login
                                                 2. Register
                                                 3. Exit            """)

        option = int(input("Enter the choice 1 or 2 or 3:\n"))
        if option == constants.USER_CHOICE_ONE:
            username = input("Enter the Username:\n")
            password = input("Enter the Password:\n")
            login = Login(username.upper(), password)
            login.login()
        elif option == constants.USER_CHOICE_TWO:
            print("You have selected 2nd option to Register to the University Restaurant")
            print("Please enter valid username, password, email and usertype[Admin, Student,Staff]")
            username = input("Enter the Username:\n")
            validate_user(valid_user_check, username)
            password = input("Enter the Password:\n")
            validate_password(valid_password_check, password)
            email = input("Enter the Email Id:\n")
            validate_email(valid_email_check, email)
            user_type = input("Enter the user type:\n")
            validate_type(valid_usertype_check, user_type)
            register = Register(username, password, email, user_type)
            register.register_user()
        else:
            print("You decided to exit the Restaurant")


if __name__ == '__main__':
    actions()
