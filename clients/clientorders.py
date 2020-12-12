from clients import client as c
from clientmenu import add_client
from food import setmenu as smenu
from food import menu
from random import randint as rand
import main

from re import search

""" CLIENT ORDERS """
client_orders = []


class ClientOrder(c.Client):
    def __init__(self, name="", surname="", email="", contact_number="", order_list=[], subtotal=0, order_id="", status="WAIT"):
        super().__init__(name, surname, email, contact_number)
        self._order_list = order_list
        self._subtotal = subtotal
        self._order_id = order_id
        self._status = status

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
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self.status = status

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        self.order_id = order_id

    def get_order(self):
        return self.order_list

    def get_status(self):
        return self.status


""" LOADING AND SAVING ORDERS """


def load_order_file(filename: str):
    try:
        pass
    except Exception as e:
        print(e)


def save_order_file(filename: str):
    try:
        with open(filename, "w") as file:
            for order in client_orders:
                temp_str = f'{order.full_info}, {order.order_list}, {order.subtotal}'
    except Exception as e:
        print(e)


def get_orders():
    """
    returns the list of clients in the database
    :return: client_list: list
    """
    return client_orders


""" ORDER FUNCTIONS """


def add_order(name, surname, email, contact, order_list, subtotal, order_id):
    client_orders.append(ClientOrder(name, surname, email, contact, order_list, subtotal, order_id))


def view_order():
    pick_order = input("What order do you want to view?\n Format(surname, name, subtotal): ")
    surname, name, subtotal = pick_order.split(", ")
    temp_order = [o for o in get_orders() if o.surname == surname and o.name == name and o.subtotal == subtotal]
    for order in temp_order:
        print(order.full_name, order.order_list, order.subtotal, order.status)


def remove_order(order_id):
    filter(lambda x: x.order_id != order_id, client_orders)


def display_orders():
    order_list = get_orders()
    for order in order_list:
        yield order.full_name, order.subtotal


def random_id():
    return rand(100000, 999999)


def check_client(name, surname, email, contact):
    if len([x for x in c.get_clients() if x.name == name and x.surname == surname]) == 0:
        add_client(name, surname, email, contact)


""" CONSOLE MESSAGES """


def display_orders_interface():
    """
    Displays the orders section
    """
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
                subtotal += lambda x: dish[-1] * int(new_order)
            order.append(tuple(list(dish), new_order))
        add_order(name, surname, email, contact, order, subtotal, random_id())
        print("Order confirmed!")




        display_orders_interface()
    else:
        main.intro_message()


if __name__ == "__main__":
    try:

        display_orders_interface()
    except Exception as e:
        print(e)
