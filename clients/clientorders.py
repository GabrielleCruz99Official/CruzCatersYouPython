from clients import client as c
from clients import clientmenu as cm
from food import setmenu as smenu
from food import menu
from random import randint as rand
import main

from re import search

""" CLIENT ORDERS """
client_orders = []


class ClientOrder(c.Client):
    def __init__(self, name="", surname="", email="", contact_number="", order_list=[], subtotal=0, order_id=0):
        super().__init__(name, surname, email, contact_number)
        self._order_list = order_list
        self._subtotal = subtotal
        self._order_id = order_id

    @property
    def order_list(self):
        return self._order_list

    @order_list.setter
    def order_list(self, order_list):
        self.order_list = order_list

    @property
    def subtotal(self):
        return self._subtotal

    @subtotal.setter
    def subtotal(self, subtotal):
        self.subtotal = subtotal

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        self.order_id = order_id


""" ORDER FUNCTIONS """


def add_order(name, surname, email, contact, order_list, subtotal, order_id):
    client_orders.append(ClientOrder(name, surname, email, contact, order_list, subtotal, order_id))


def view_order():
    pick_order = input("What order do you want to view?\n ID: ")
    temp_order = [o for o in client_orders if o.order_id == pick_order]
    for order in temp_order:
        print(order.full_name(), order.order_list, order.subtotal)


def clear_orders():
    client_orders.clear()


def display_orders():
    order_list = get_orders()
    for order in order_list:
        yield order.full_name(), order.order_list, order.subtotal, order.order_id


def random_id():
    """
    This is the random id generator for each new order
    :return: a random integer between 100000 and 999999
    """
    return rand(100000, 999999)


def check_client(name, surname, email, contact):
    if len([x for x in c.get_clients() if x.name == name and x.surname == surname]) == 0:
        cm.add_client(name, surname, email, contact)


""" LOADING AND SAVING ORDERS """


def load_order_file(filename: str):
    try:
        with open(filename, "r") as file:
            for line in file:
                order_start = line.find("[")
                order_end = line.find("]") + 1
                order_list = line[order_start:order_end]
                # added 2 to the index of order_end to skip
                # whitespace and comma
                rest = line[:order_start] + line[order_end + 2:]
                full_name, email, contact, subtotal, order_id = rest.rstrip().split(", ")
                name, surname = full_name.split(" ")
                add_order(name, surname, email, contact, order_list, subtotal, order_id)
    except Exception as e:
        print(e)


def save_order_file(filename: str):
    try:
        with open(filename, "w") as file:
            for order in client_orders:
                temp_str = f'{order.full_info()}, {order.order_list}, {order.subtotal}, {order.order_id}\n'
                file.writelines(temp_str)
    except Exception as e:
        print(e)


def get_orders():
    """
    returns the list of clients in the database
    :return: client_list: list
    """
    return client_orders


def load_orders():
    client_orders = []
    load_order_file("data\clientorders.txt")


def save_orders():
    save_order_file("data\clientorders.txt")


""" CONSOLE MESSAGES """


def display_orders_interface():
    """
    Displays the orders section
    """
    load_orders()
    print("======\nORDERS\n======")
    for order in display_orders():
        print(order)
    ui_choice = input("What do you want to do?\n1: View Order\n2: Add New Order\nType anything else to return: ")
    if ui_choice == "1" or ui_choice.lower() == "view":
        try:
            view = True
            while view:
                view_order()
                again = input("Do you want to view another order? Y/N: ")
                if again.lower() == "no" or again.lower() == "n":
                    view = False
        except Exception as e:
            print(e)
        finally:
            print("There was an error in your input. Redirected to main page.")
            display_orders_interface()
    elif ui_choice == "2" or ui_choice.lower() == "add":
        print("====\nMENU\n====")
        menu.load_menu()
        menu.load_menu_dishes()
        week_menu = smenu.weekly_menu_to_list()
        print("============")
        client = input("Input contact details in this format\n(Name, Surname, Email, Contact Number): ")
        name, surname, email, contact = client.split(", ")
        order = []
        subtotal = 0
        for dish in week_menu:
            new_order = input(f'{dish} - Quantity: ')
            if search("[^0-9]", new_order):
                print("You didn't put an integer.")
                display_orders_interface()
            temp_list = list(dish)
            subtotal += int(dish[-1]) * int(new_order)
            temp_list.append(new_order)
            order.append(tuple(temp_list))
        add_order(name, surname, email, contact, order, subtotal, random_id())
        save_orders()
        print("Order confirmed!")
        display_orders_interface()
    else:
        main.intro_message()


if __name__ == "__main__":
    try:
        display_orders_interface()
    except Exception as e:
        print(e)
