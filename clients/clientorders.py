from clients import client as c
from food import setmenu as smenu
from food import menu
import main

from re import search

""" CLIENT ORDERS """
client_orders = []


class ClientOrder(c.Client):
    def __init__(self, name="", surname="", email="", contact_number = "", order_list=[], subtotal=0, status="WAIT"):
        super().__init__(name, surname, email, contact_number)
        self.order_list = order_list
        self.subtotal = subtotal
        self.status = status

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


def add_order(name, surname, email, contact, order_list, subtotal):
    client_orders.append(ClientOrder(name, surname, email, contact, order_list, subtotal))


def view_order():
    pick_order = input("What order do you want to view?\n Format(surname, name, subtotal): ")
    surname, name, subtotal = pick_order.split(", ")
    temp_order = [o for o in get_orders() if o.surname == surname and o.name == name and o.subtotal == subtotal]
    for order in temp_order:
        print(order.full_name, order.order_list, order.subtotal, order.status)


def create_order():
    pass


def display_orders():
    order_list = get_orders()
    for order in order_list:
        yield order.full_name, order.subtotal


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
        print("================\nMENU OF THE WEEK\n================")
        menu.load_menu()
        menu.load_menu_dishes()

        display_orders_interface()
    else:
        main.intro_message()


if __name__ == "__main__":
    try:

        display_orders_interface()
    except Exception as e:
        print(e)
