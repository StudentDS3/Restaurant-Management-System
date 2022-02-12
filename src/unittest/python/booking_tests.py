import sys
sys.path.append('C:/Users/User/Documents/Restaurant-Management-System/src')
sys.path.append('C:/Users/User/Documents/Restaurant-Management-System/src/main/python')
from unittest import TestCase
import unittest
import re

from booking import Register, validate_user, validate_password, validate_email, validate_type, Login

class TestRegister(TestCase):

    def setUp(self):
        self.reg_admin = Register('User1', 'user10123', 'user1@gmail.com', 'Admin')
        self.reg_student = Register('User2', 'user2@1234', 'user2@gmail.com', 'Student')

    def test_register_user(self):
        self.assertEqual(self.reg_admin.username, 'User1')
        self.assertEqual(self.reg_admin.password, 'user10123')
        self.assertEqual(self.reg_admin.email, 'user1@gmail.com')
        self.assertEqual(self.reg_admin.type, 'Admin')
        self.assertEqual(self.reg_student.username, 'User2')
        self.assertEqual(self.reg_student.password, 'user2@1234')
        self.assertEqual(self.reg_student.email, 'user2@gmail.com')
        self.assertEqual(self.reg_student.type, 'Student')


valid_user_check = lambda uname: True if re.match("^[a-zA-Z0-9_]+$", uname) else False

valid_password_check = lambda passwd: True if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', passwd) else False

valid_email_check = lambda mail: True if re.search(r'[\w.-]+@[\w.-]+.\w+', mail) else False

valid_usertype_check = lambda type_of_user: True if any(
    word in type_of_user for word in ['student', 'staff', 'admin']) else False


class TestValidations(TestCase):
    def test_validate_user(self):
        try:
            self.assertIsNone(validate_user(valid_user_check, "user1"))
        except SystemExit:
            self.assertRaises(SystemExit)

    def test_validate_password(self):
        try:
            self.assertTrue(validate_password(valid_password_check, "us0123"))
        except SystemExit:
            self.assertRaises(SystemExit)

    def test_validate_email(self):
        try:
            self.assertTrue(validate_email(valid_email_check, "user.gmail.com"))
        except SystemExit:
            self.assertRaises(SystemExit)

    def test_validate_type(self):
        try:
            self.assertTrue(validate_type(valid_usertype_check, "user"))
        except SystemExit:
            self.assertRaises(SystemExit)

    def test_user_admin(self):
        self.assertIsNone(validate_user(valid_user_check, "User1"))

    def test_password_admin(self):
        self.assertIsNone(validate_user(valid_password_check, "user10123"))

    def test_email_admin(self):
        self.assertIsNone(validate_user(valid_email_check, "user1@gmail.com"))


class TestLogin(TestCase):
    def setUp(self):
        self.log = Login('User1', 'user10123')
        self.log1 = Login('User2', 'user2@1234')
        self.log2 = Login('user3', 'cc@123456')

    def test_user_condition(self):
        self.assertTrue(self.log.user_condition('User1', 'user10123'))
        self.assertFalse(self.log.user_condition('User1', '321fdd0sd'))

    def test_check_admin_login(self):
        try:
            self.assertEquals("None", self.log.check_user(), "ADMIN")
        except FileNotFoundError:
            self.assertRaises(FileNotFoundError)

    def test_check_student_login(self):
        try:
            self.assertEquals("STUDENT", self.log1.check_user(), "STUDENT")
        except FileNotFoundError:
            self.assertRaises(FileNotFoundError)

    def test_check_staff_login(self):
        try:
            self.assertEquals("STAFF", self.log2.check_user(), "STAFF")
        except FileNotFoundError:
            self.assertRaises(FileNotFoundError)


if __name__ == '__main__':
    unittest.main()
