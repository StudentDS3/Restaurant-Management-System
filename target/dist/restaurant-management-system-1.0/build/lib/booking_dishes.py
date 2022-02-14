import datetime
import os
import constants

directory = os.path.dirname(__file__)

issued_dish_path = os.path.join(directory, 'C:/Users/User/Documents/Restaurant-Management-System/src/database/IssuedDish.txt')
dishes_db_path = os.path.join(directory, 'C:/Users/User/Documents/Restaurant-Management-System/src/database/Menu.txt')


class Menu:
    def __init__(self, uname):
        self.dish_list = list_of_dishes()
        self._username = uname

    def display_menu(self):
        print("The dishes of the day menu at the  University Restaurant are :")
        for dish in list_of_dishes():
            print(dish)

    def order_dish(self, dish_name):
        found = [dish[0] == dish_name for dish in self.dish_list]
        if found:
            issued_date = datetime.datetime.today()
            return_date = datetime.datetime.today() + datetime.timedelta(days=constants.NUMBER_OF_DAYS)
            with open(issued_dish_path, "a+") as f:
                f.write(self._username + "," + dish_name + "," + str(issued_date) + "," + str(return_date))
                f.write("\n")
            print(f"You have ordered {dish_name} and you have till 15:00 for the pick up. Please be on time "
                  f"otherwise 5 EURO fine will be charged and  must be paid within next seven days  plus 1 EURO/Day fine for delay of paiment ")

    def cancel_order(self, dish_name, username):
        calculate_fine(username, dish_name)
        update_issued_dish_data(username, dish_name)

    def search_by_dish_name(self, dish_name):
        for dish in self.dish_list:
            if dish_name == dish[0]:
                return True
        return False

    def add_dish(self, dish, ingredients, discount, price):
        with open(dishes_db_path, "a+") as bf:
            bf.write("\n")
            bf.write(dish + "," + ingredients + "," + discount + "," + "€" + price)
            print(f"\n{dish} successfully added to database")

    def remove_dish(self, dish, ingredients):
        with open(dishes_db_path, "r+") as f:
            dishes = f.readlines()
            f.seek(0)
            for b in dishes:
                if dish not in b and ingredients not in b:
                    f.write(b)
            f.truncate()
            print(f"\n{dish} successfully deleted from the database")


def list_of_dishes():
    dishes = []
    with open(dishes_db_path, "r") as bf:
        dish_list = bf.readlines()
        [dishes.append(split_dishes_by_newline(dish)) for dish in dish_list]
        return dishes


split_dishes_by_newline = lambda x: x.replace('\n', '').split(',')


def fine_calc_decorator(func):
    def fine_function_wrapper(user, dish):
        fine = func(user, dish)
        if fine is None or fine == constants.FINE_ZERO:
            print(f"You have {fine} Euro fine !!! for the dish {dish}")
        else:
            print(f"You have {fine} Euro fine !!! ")

    return fine_function_wrapper


@fine_calc_decorator
def calculate_fine(user_name, dish_name):
    with open(issued_dish_path, "r") as f:
        dish_list = f.readlines()
        for dish in dish_list:
            dish_data = dish.split(",")
            if dish_data[0] == user_name.upper() and dish_data[1] == dish_name:
                dish_data[3] = dish_data[3].strip('\n')
                issued_date = datetime.datetime.strptime(dish_data[2], constants.DATE_FORMAT_FOR_FINE_CALC)
                return_date = datetime.datetime.strptime(dish_data[3], constants.DATE_FORMAT_FOR_FINE_CALC)
                fine = constants.NUMBER_OF_DAYS - abs(issued_date.day - return_date.day) 
                money = constants.FINE_ZERO
                if fine < constants.FINE_ZERO:
                    money = abs(fine)
                return money 


def update_issued_dish_data(user_name, dish_name):
    with open(issued_dish_path, "r+") as f:
        dishes = f.readlines()
        f.seek(0)
        found = False
        for issued_dish in dishes:
            if user_name in issued_dish and dish_name in issued_dish:
                f.truncate()
                found = True
                print(f"\n{dish_name} order is cancelled")
            else:
                f.write(issued_dish)
        if not found:
            print(f"\n Hey!! {user_name} No {dish_name} has not been ordered to you!")
