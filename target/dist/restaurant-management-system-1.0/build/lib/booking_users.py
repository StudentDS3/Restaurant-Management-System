from booking_dishes import Menu, calculate_fine
import constants


class User:
    def __init__(self, username, access_type):
        self._username = username
        self._access_type = access_type
        self.b1 = Menu(self._username)

    def student_staff_actions(self):
        while True:
            print("Below the diffrerent options  on the account!")
            print("1", "Display menu")
            print("2", "Search dish By dish Name")
            print("3", "Order a dish")
            print("4", "Cancel order")
            print("5", "pay fine")
            print("Press any number for exit")
            student_staff_decision = input("Enter your choice \n")
            if student_staff_decision not in ["1", "2", "3", "4", "5"]:
                print("You have selected different choice and logging out from the system")
                exit()
            else:
                student_staff_decision = int(student_staff_decision)
                self.user_decisions(self.b1, student_staff_decision)

    def user_decisions(self, b1, user_choice):
        if user_choice == constants.USER_CHOICE_ONE:
            b1.display_menu()
            print("\n")

        elif user_choice == constants.USER_CHOICE_TWO:
            dish_name = input("Enter the name of dish: ")
            if b1.search_by_dish_name(dish_name):
                print(f"\n The dish {dish_name} is found !! \n")
            else:
                print(f"\nThe dish {dish_name} your searching is not found !! give it another short\n")

        elif user_choice == constants.USER_CHOICE_THREE:
            dish = input("please Enter the name of the dish you want to order :")
            b1.order_dish(dish)
            print("\n")

        elif user_choice == constants.USER_CHOICE_FOUR:
            dish = input("please Enter the name of the dish you want to cancel :")
            user = input("please enter your name:")
            b1.cancel_order(dish, user.upper())
            print("\n")

        elif user_choice == constants.USER_CHOICE_FIVE:
            dish = input("please Enter the name of the dish having fine :")
            calculate_fine(self._username, dish)

    def admin_actions(self):
        while True:
            print("Below the diffrerent options  on the account as admin!")
            print("1", "Display a dish")
            print("2", "Add a dish")
            print("3", "Remove a dish")
            print("Press any number for exit")
            admin_choice = int(input("Enter your choice \n"))
            if admin_choice == constants.USER_CHOICE_ONE:
                self.b1.display_menu()
                print("\n")

            elif admin_choice == constants.USER_CHOICE_TWO:
                dish_name = input("Enter the name of dish : ")
                ingredients = input("Enter the dish ingredients :  ")
                discount = input("Enter the discount for the dish :  ")
                price = input("Enter the price of the dish : ")
                self.b1.add_dish(dish_name, ingredients, discount, price)

            elif admin_choice == constants.USER_CHOICE_THREE:
                dish = input("please Enter the name of the dish you want to delete :")
                ingredients = input("please Enter the dish ingredients :")
                self.b1.remove_dish(dish, ingredients)
                print("\n")

            else:
                exit()
