from food import menu
from debug import exceptions as exc
from clients import clientmenu as cl
from clients import clientorders as ord
import tkinter as tk
import sys


"""CONSOLE MESSAGES"""


def load_main_menu():
    """
    This function displays the application's main menu.
    """
    intro_message()


def intro_message():
    """
    This function displays the main menu in the console interface.
    """
    print("\n=============\nCRUZCATERSYOU\n=============")
    mode_select = input("Select mode:\n1: Menu\n2: Clients\n3: Orders\nType anything else to exit: ")
    if mode_select == "1" or mode_select.lower() == "menu":
        # this displays the menu and dishes interface
        menu.display_menu_interface()
    if mode_select == "2" or mode_select.lower() == "client":
        # this displays the client interface
        cl.display_clients_interface()
    if mode_select == "3" or mode_select.lower() == "order":
        # this displays the orders interface
        ord.display_orders_interface()
    else:
        print("Goodbye!")
        # inserted the line below to stop the intro message from displaying twice
        sys.exit(1)


"""GUI"""


def load_main_gui():
    window = tk.Tk()
    window.title("CRUZCATERSYOU")
    window.geometry("200x150")
    main = MainMenu(master=window)
    window.mainloop()


class MainMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # main menu label
        self.title_card = tk.Label(self, text="============\nCRUZCATERSYOU\n============")
        self.title_card.pack(side="top")

        # menu button
        self.menu = tk.Button(self, text="Menu")
        self.menu.bind("<Button>", lambda e: Menu(self))
        # self.menu["command"] = self.load_menu
        self.menu.pack()

        # clients button
        self.clients = tk.Button(self)
        self.clients["text"] = "Clients"
        # self.clients["command"] = self.load_clients
        self.clients.pack()

        # orders button
        self.orders = tk.Button(self)
        self.orders["text"] = "Orders"
        # self.orders["command"] = self.load_orders
        self.orders.pack()

        # quit button
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def load_menu(self):
        menu.display_menu_interface()

    def load_clients(self):
        cl.display_clients_interface()

    def load_orders(self):
        ord.display_orders_interface()


class Menu(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Menu")
        self.geometry("450x450")
        self.label_text = tk.Label(self, text="===================\nMENU AND FOOD IDEAS\n===================")
        self.label_text.pack()

        self.back = tk.Button(self, text="Return")
        self.back["command"] = self.withdraw()
        self.back.pack()


class Clients(tk.Toplevel):
    pass


class Orders(tk.Toplevel):
    pass


if __name__ == "__main__":
    try:
        # load_main_menu()
        load_main_gui()
    except Exception as e:
        print(e)
    except exc.IDError as idE:
        print(idE)
