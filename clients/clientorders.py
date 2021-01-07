from clients import client as c
from clients import clientmenu as cm
from food import setmenu as smenu
from food import menu
from random import randint as rand
import main
import logging as log

from re import search

""" CLIENT ORDERS """
client_orders = []


class ClientOrder:
    def __init__(self, main_client, order_list=[], subtotal=0, order_id=0):
        self.client = main_client
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

    def relevant_info(self):
        return f'{self.client.client_id}, {self.order_list}, {self.subtotal}, {self.order_id}'


""" ORDER FUNCTIONS """


def add_order(old_client, order_list: list, subtotal: int, order_id: int):
    """
    Adds an existing client's new order to the database

    Precondition
    ------------
    The client must already be in the database

    Postcondition
    -------------
    - The order is added into the database.
    """
    client_orders.append(ClientOrder(old_client, order_list, subtotal, order_id))


def clear_orders():
    client_orders.clear()


def display_orders():
    """
    Displays the list of orders using a generator
    """
    order_list = get_orders()
    for order in order_list:
        yield order.client.full_info(), order.order_list, order.subtotal, order.order_id


def random_id():
    """
    This is the random id generator for each new order
    :return: a random integer between 100000 and 999999
    """
    return rand(100000, 999999)


""" LOADING AND SAVING ORDERS """


def load_order_file(filename: str):
    """
    This function loads the list of orders from the database

    Precondition
    ------------
    The target file must already exist.

    Postcondition
    -------------
    - The order list will contain the orders kept in the database
    - If the file cannot be found, an exception will be raised
    - If the file cannot be loaded, an IOError will be raised
    """
    try:
        with open(filename, "r") as file:
            for line in file:
                order_start = line.find("[")
                order_end = line.find("]") + 1
                order_list = line[order_start:order_end]
                # added 2 to the index of order_end to skip
                # whitespace and comma
                rest = line[:order_start] + line[order_end+2:]
                client_id, subtotal, order_id = rest.rstrip().split(", ")
                client_info = check_client(int(client_id))
                add_order(client_info, order_list, subtotal, order_id)
    except FileNotFoundError:
        log.error("File cannot be found.")
    except IOError:
        log.error("Orders cannot be loaded.")
    else:
        log.info("Order list loaded.")


def save_order_file(filename: str):
    """
    This function will save the list of orders
    into the database

    Precondition
    ------------
    The target file must exist.

    Postcondition
    -------------
    The target file will contain the list of orders.
    If the target file doesn't exist, the program will
    create one.
    If the list cannot be saved, an error will be raised.
    """
    try:
        with open(filename, "w") as file:
            for order in client_orders:
                temp_str = f'{order.relevant_info()}\n'
                file.writelines(temp_str)
    except IOError:
        log.error("Orders cannot be saved")
    else:
        log.info("Orders saved to database")


def get_orders() -> list:
    """
    returns the list of clients in the database
    :return: client_list: list
    """
    return client_orders


def load_orders():
    load_order_file("data\clientorders.txt")


def save_orders():
    save_order_file("data\clientorders.txt")


"""
The next two functions are used to check
if the client is already in the database
before adding their order.
"""


def existing_client() -> c.Client:
    exist = input("If it's a returning client, input their ID: ")
    temp_id = int(exist)
    return check_client(temp_id)


def check_client(client_id: int) -> list:
    check = [x for x in c.client_list if x.client_id == int(client_id)]
    return check[0]


""" CONSOLE MESSAGES """


def display_orders_interface():
    """
    Displays the orders section
    """
    clear_orders()
    cm.load_client_list()
    load_orders()
    print("======\nORDERS\n======")
    for order in display_orders():
        print(order)
    ui_choice = input("What do you want to do?\n1: Add New Order\nType anything else to return: ")
    if ui_choice == "1" or ui_choice.lower() == "add":
        print("====\nMENU\n====")
        menu.load_menu()
        menu.load_menu_dishes()
        week_menu = smenu.weekly_menu_to_list()
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
        exist = input("Is it a returning client? ")
        if exist.lower() == "yes" or exist.lower() == "y":
            old_client = existing_client()
            add_order(old_client, order, subtotal, random_id())
            print("Order confirmed!")
        else:
            log.warning("Client should be added first.")
        display_orders_interface()
    else:
        save_orders()
        main.intro_message()


if __name__ == "__main__":
    display_orders_interface()
