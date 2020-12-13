from food import menu as m
from food import setmenu as sm
from food import items as it
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
        m.display_menu_interface()
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
        self.load_database()
        self.create_widgets()


    def create_widgets(self):
        # main menu label
        self.title_card = tk.Label(self, text="============\nCRUZCATERSYOU\n============")
        self.title_card.pack(side="top")

        # menu button
        self.menu = tk.Button(self, text="Menu")
        self.menu.bind("<Button>", lambda x: Menu(self.master))
        # self.menu["command"] = self.load_menu
        self.menu.pack()

        # clients button
        self.clients = tk.Button(self, text="Clients")
        self.clients.bind("<Button>", lambda x: Clients(self.master))
        # self.clients["command"] = self.load_clients
        self.clients.pack()

        # orders button
        self.orders = tk.Button(self, text="Orders")
        self.orders.bind("<Button>", lambda x: Orders(self.master))
        # self.orders["command"] = self.load_orders
        self.orders.pack()

        # quit button
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def load_database(self):
        m.load_items()
        cl.load_client_list()
        ord.load_orders()

    def load_menu(self):
        m.display_menu_interface()

    def load_clients(self):
        cl.display_clients_interface()

    def load_orders(self):
        ord.display_orders_interface()


class Menu(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Menu")
        self.geometry("450x450")
        self.create_widgets()

    def create_widgets(self):
        """TITLE FRAME"""
        self.title_frame = tk.Frame(self, borderwidth=2, relief='ridge')
        self.title_frame.pack(side="top")
        self.menu_label = tk.Label(self.title_frame, text="========\nMENU AND FOOD IDEAS\n========")
        self.menu_label.pack()
        self.week_menu = tk.Listbox(self.title_frame, width=0, height=0)
        wm = sm.weekly_menu_to_list()
        for menu_dish in wm:
            self.week_menu.insert(wm.index(menu_dish), f'{menu_dish[0]}: {menu_dish[-1]}')
        self.week_menu.pack()

        """DISHES FRAME"""
        self.dish_frame = tk.Frame(self, borderwidth=2, relief='ridge')
        self.dish_frame.pack(side="left")
        self.dish_label = tk.Label(self.dish_frame, text="-Dish Ideas-")
        self.dish_label.pack()
        # display all dish ideas in this listbox
        self.dish_box = tk.Listbox(self.dish_frame, width=0, height=0)
        self.dish_box.pack()
        # press this button to update list of dish ideas
        self.display_dishes = tk.Button(self.dish_frame, text="Display Dishes", fg="orange")
        self.display_dishes.bind("<Button>", self.update_dishes())
        self.display_dishes.pack()

        """FRAME FOR ADDING NEW DISHES"""
        self.add_dish_frame = tk.Frame(self.dish_frame, borderwidth=1, relief='ridge')
        self.add_dish_frame.pack(side="left")
        self.add_dish_frame_label = tk.Label(self.add_dish_frame, text="Add new dish?")
        self.add_dish_frame_label.pack(side="top")
        self.add_id_label = tk.Label(self.add_dish_frame, text="Dish ID")
        self.add_id_label.pack()
        self.add_id = tk.Entry(self.add_dish_frame)
        self.add_id.pack()
        self.add_name_label = tk.Label(self.add_dish_frame, text="Dish Name")
        self.add_name_label.pack()
        self.add_name = tk.Entry(self.add_dish_frame)
        self.add_name.pack()
        self.add_price_label = tk.Label(self.add_dish_frame, text="Dish Price")
        self.add_price_label.pack()
        self.add_price = tk.Entry(self.add_dish_frame)
        self.add_price.pack()
        self.add_new_dish = tk.Button(self.add_dish_frame, text="Confirm")
        self.add_new_dish.bind("<Button>", self.add_dish)
        self.add_new_dish.pack()

        """FRAME TO REMOVE EXISTING DISH"""
        self.remove_dish_frame = tk.Frame(self.dish_frame, borderwidth=1, relief='ridge')
        self.remove_dish_frame.pack(side="left")
        self.remove_dish_frame_label = tk.Label(self.remove_dish_frame, text="Remove a dish?")
        self.remove_dish_frame_label.pack(side="top")
        self.remove_id_label = tk.Label(self.remove_dish_frame, text="Dish ID")
        self.remove_id_label.pack()
        self.remove_id = tk.Entry(self.remove_dish_frame)
        self.remove_id.pack()
        self.remove_new_dish = tk.Button(self.remove_dish_frame, text="Confirm")
        self.remove_new_dish.bind("<Button>", self.remove_dish)
        self.remove_new_dish.pack()

        """RETURN TO MAIN MENU"""
        self.menu_back = tk.Button(self, text="Return", fg="red")
        self.menu_back.bind('<Button>', self.go_back)
        self.menu_back.pack(side="bottom")

    def add_dish(self, event):
        it.add_item(self.add_id.get(), self.add_name.get(), int(self.add_price.get()))
        self.update_dishes()

    def remove_dish(self, event):
        it.remove_item(self.remove_id.get())
        self.update_dishes()

    def update_dishes(self):
        self.dish_box.delete(0, tk.END)
        di = it.food_idea_to_list()
        for dish in di:
            self.dish_box.insert(di.index(dish), '{}- {}: {}'.format(dish[0], dish[1]['name'], dish[1]['price']))

    def go_back(self, event):
        m.save_dish()
        m.save_menu()
        self.withdraw()
        print("Back to main menu.")

class Clients(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Orders")
        self.geometry("450x450")
        self.create_widgets()

    def create_widgets(self):
        self.client_label = tk.Label(self, text="=======\nCLIENTS\n=======")
        self.client_label.pack()

        self.client_back = tk.Button(self, text="Return", fg="red")
        self.client_back.bind('<Button>', self.go_back)
        self.client_back.pack()

    def go_back(self, event):
        print("Back to main menu.")
        self.withdraw()


class Orders(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Menu")
        self.geometry("450x450")
        self.create_widgets()

    def create_widgets(self):
        self.order_label = tk.Label(self, text="======\nOrders\n======")
        self.order_label.pack()

        self.order_back = tk.Button(self, text="Return", fg="red")
        self.order_back.bind('<Button>', self.go_back)
        self.order_back.pack()

    def go_back(self, event):
        print("Back to main menu.")
        m.save_menu()
        m.save_dish()
        self.withdraw()


if __name__ == "__main__":
    try:
        # load_main_menu()
        load_main_gui()
    except Exception as e:
        print(e)
    except exc.IDError as idE:
        print(idE)
