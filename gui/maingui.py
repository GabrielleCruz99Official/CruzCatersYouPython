import tkinter as tk
from food import menu as m
from clients import clientmenu as cl
from clients import clientorders as o
from gui import menugui as mg
from gui import clientgui as cg
from gui import ordergui as og


# Here, we find the window of our application's main menu
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
        self.menu.bind("<Button>", lambda x: mg.Menu(self.master))
        self.menu.pack()

        # clients button
        self.clients = tk.Button(self, text="Clients")
        self.clients.bind("<Button>", lambda x: cg.Clients(self.master))
        self.clients.pack()

        # orders button
        self.orders = tk.Button(self, text="Orders")
        self.orders.bind("<Button>", lambda x: og.Orders(self.master))
        self.orders.pack()

        # quit button
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    """
    Every time we start our application, the database is loaded
    """
    def load_database(self):
        m.load_items()
        cl.load_client_list()
        o.load_orders()