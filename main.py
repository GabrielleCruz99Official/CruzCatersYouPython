from apptest import *
from clients import saveclient
from food import menu
from gui import *

def load_main_menu():
    """
    This function displays the application's main menu.
    """

    menu.display_interface()

if __name__ == "__main__":
    load_main_menu()