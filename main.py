from gui import maingui as app
from debug import exceptions as exc
from food import menu as m
from clients import clientmenu as cl
from clients import clientorders as o
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
        m.display_menu_interface()
    if mode_select == "2" or mode_select.lower() == "client":
        # this displays the client interface
        cl.display_clients_interface()
    if mode_select == "3" or mode_select.lower() == "order":
        # this displays the orders interface
        o.display_orders_interface()
    else:
        print("Goodbye!")
        # inserted the line below to stop the intro message from displaying twice
        sys.exit(1)


""" GRAPHICAL USER INTERFACE """


# settings for the application's main window
def load_main_gui():
    window = tk.Tk()
    window.title("CRUZCATERSYOU")
    window.geometry("200x150")
    main = app.MainMenu(master=window)
    window.mainloop()


"""
The application has three subsections (menu, clients, and orders) placed
in separate windows that are originally hidden whenever the application
is opened. Whenever you click one of the buttons in the main menu,
the corresponding window will appear.
"""


if __name__ == "__main__":
    try:
        # load_main_menu()
        load_main_gui()
    except exc.IDError as idE:
        print(idE)
    except Exception as e:
        print(e)
