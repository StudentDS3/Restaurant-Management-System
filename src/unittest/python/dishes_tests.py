import sys
sys.path.append('C:/Users/User/Documents/Restaurant-Management-System/src')
sys.path.append('C:/Users/User/Documents/Restaurant-Management-System/src/main/python')
import unittest
from unittest import TestCase
from booking_dishes import Menu


class TestMenu(TestCase):

    def test_display_menu(self):
        try:
            self.bk = Menu('Hina')
            self.bk.display_menu()
        except FileNotFoundError:
            self.assertRaises(FileNotFoundError)


if __name__ == '__main__':
    unittest.main()
