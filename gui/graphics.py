import tkinter as tk
from food import menu as m
from food import setmenu as sm
from debug import exceptions as exc
from clients import clientmenu as cl
from clients import clientorders as ord


def load():
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
        self.load_database()

    def create_widgets(self):
        # main menu label
        self.title_card = tk.Label(self, text="============\nCRUZCATERSYOU\n============")
        self.title_card.pack(side="top")

        # menu button
        self.menu = tk.Button(self, text="Menu")
        self.menu.pack()

        # clients button
        self.clients = tk.Button(self)
        self.menu.bind("<Button>", lambda x: Clients(self.master))
        self.clients.pack()

        # orders button
        self.orders = tk.Button(self)
        self.menu.bind("<Button>", lambda x: Orders(self.master))
        self.orders.pack()

        # quit button
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def load_database(self):
        m.load_menu()
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
        self.label_text = tk.Label(self, text="===================\nMENU AND FOOD IDEAS\n===================")
        self.label_text.pack()
        self.week_menu = tk.Listbox(self, width=25, height=8)
        wm = sm.weekly_menu_to_list()
        for menu_dish in wm:
            self.week_menu.insert(wm.index(menu_dish), f'{menu_dish[0]}: {menu_dish[-1]}')
        self.week_menu.pack()
        self.back = tk.Button(self, text="Return")
        self.back.bind('<Button>', self.go_back)
        self.back.pack()

    def go_back(self, event):
        print("Back to main menu.")
        self.withdraw()


class Clients(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Orders")
        self.geometry("450x450")
        self.create_widgets()

    def create_widgets(self):
        self.label_text = tk.Label(self, text="===================\nMENU AND FOOD IDEAS\n===================")
        self.label_text.pack()
        self.week_menu = tk.Listbox(self, width=25, height=8)
        wm = sm.weekly_menu_to_list()
        for menu_dish in wm:
            self.week_menu.insert(wm.index(menu_dish), f'{menu_dish[0]}: {menu_dish[-1]}')
        self.week_menu.pack()
        self.back = tk.Button(self, text="Return")
        self.back.bind('<Button>', self.go_back)
        self.back.pack()

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
        self.label_text = tk.Label(self, text="===================\nMENU AND FOOD IDEAS\n===================")
        self.label_text.pack()
        self.week_menu = tk.Listbox(self, width=25, height=8)
        wm = sm.weekly_menu_to_list()
        for menu_dish in wm:
            self.week_menu.insert(wm.index(menu_dish), f'{menu_dish[0]}: {menu_dish[-1]}')
        self.week_menu.pack()
        self.back = tk.Button(self, text="Return")
        self.back.bind('<Button>', self.go_back)
        self.back.pack()

    def go_back(self, event):
        print("Back to main menu.")
        self.withdraw()

if __name__ == "__main__":
    try:
        """
        window = tk.Tk()
        app = App(master=window)
        app.mainloop()
        """
    except Exception as e:
        print(e)