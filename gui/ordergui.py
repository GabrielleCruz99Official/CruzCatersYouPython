import tkinter as tk
from clients import clientorders as o
from food import setmenu as sm


class Orders(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Orders")
        self.geometry("450x600")
        self.create_widgets()

    def create_widgets(self):
        self.order_label = tk.Label(self, text="======\nOrders\n======")
        self.order_label.pack()

        """ORDERS FRAME"""
        self.order_frame = tk.Frame(self, borderwidth=2, relief='ridge')
        self.order_frame.pack(side="top")
        self.order_list_label = tk.Label(self.order_frame, text="-order List-")
        self.order_list_label.pack()

        self.order_list = OrderRadio(self.order_frame)
        self.order_list.pack(side="left")

        self.view_order = tk.Button(self.order_list, text="Display Order")
        self.view_order.bind("<Button>", self.display_order)
        self.view_order.pack(side="bottom")

        self.order_info = tk.Listbox(self.order_frame, width=0, height=0)
        self.order_info.pack(side="right")

        """ ADDING AND REMOVING ORDERS """
        self.change_orders_list = tk.Frame(self, borderwidth=2, relief='ridge')
        self.change_orders_list.pack(side="top")

        self.change_orders_label = tk.Label(self.change_orders_list, text='-Add or Remove Orders-')
        self.change_orders_label.pack(side="top")

        """ADDING A NEW ORDER"""
        self.add_order = tk.Frame(self, borderwidth=1, relief='ridge')
        self.add_order.pack(side="left")
        self.add_order_label = tk.Label(self.add_order, text="Add New Order")
        self.add_order_label.pack(side="top")

        """ PERSONAL INFO """
        self.name_label = tk.Label(self.add_order, text="Name")
        self.name_label.pack()
        self.add_client_name = tk.Entry(self.add_order)
        self.add_client_name.pack()

        self.surname_label = tk.Label(self.add_order, text="Surname")
        self.surname_label.pack()
        self.add_client_surname = tk.Entry(self.add_order)
        self.add_client_surname.pack()

        self.email_label = tk.Label(self.add_order, text="Email")
        self.email_label.pack()
        self.add_client_email = tk.Entry(self.add_order)
        self.add_client_email.pack()

        self.contact_label = tk.Label(self.add_order, text="Contact")
        self.contact_label.pack()
        self.add_client_contact = tk.Entry(self.add_order)
        self.add_client_contact.pack()

        """PUTTING THE QUANTITY FOR EACH DISH"""
        self.week_menu = tk.Frame(self.add_order, borderwidth=1, relief='ridge')
        self.week_menu.pack(side="right")

        self.week_menu_list = WeekMenu(self.week_menu)
        self.week_menu_list.pack()

        self.order_confirm = tk.Button(self.week_menu, text="Confirm")
        self.order_confirm.bind("<Button>", self.add_new_order)
        self.order_confirm.pack(side="bottom")

        self.order_back = tk.Button(self, text="Return", fg="red")
        self.order_back.bind('<Button>', self.go_back)
        self.order_back.pack()

        """REMOVING AN ORDER"""
        self.remove_order = tk.Frame(self, borderwidth=1, relief='ridge')
        self.remove_order.pack()
        self.remove_order_label = tk.Label(self.remove_order, text="Clear Orders?")
        self.remove_order_label.pack(side="top")

        self.remove_confirm = tk.Button(self.remove_order, text="Confirm")
        self.remove_confirm.bind("<Button>", self.clear_order)
        self.remove_confirm.pack(side="bottom")

    def clear_order(self, event):
        o.clear_orders()

    def add_new_order(self, event):
        quantity = list(self.week_menu_list.get_qty())
        week_menu = sm.weekly_menu_to_list()
        subtotal = 0
        order = []
        for dish in week_menu:
            temp = list(dish)
            index = week_menu.index(dish)
            temp.append(quantity[index])
            subtotal += int(dish[1]) * int(quantity[index])
            order.append(tuple(temp))
        o.add_order(self.add_client_name.get(), self.add_client_surname.get(), self.add_client_email.get(),
                    self.add_client_contact.get(), order, subtotal, o.random_id())

    def display_order(self, event):
        self.order_info.delete(0, tk.END)
        order_id = self.order_list.view_info()
        picked = [x for x in o.get_orders() if x.order_id == order_id]
        for order in picked:
            temp_text_1 = 'Name: {}'.format(order.full_name())
            temp_text_2 = 'Order: {}'.format(order.order_list)
            temp_text_3 = 'Subtotal: {}€'.format(order.subtotal)
            self.order_info.insert(0, temp_text_1)
            self.order_info.insert(1, temp_text_2)
            self.order_info.insert(2, temp_text_3)

    def go_back(self, event):
        print("Back to main menu.")
        o.save_orders()
        self.withdraw()


class WeekMenu(tk.Frame):
    """
    This will load the menu of the week into
    the orders interface and it will get
    the quantity of each dish.
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.quantity = []
        self.week_menu = sm.weekly_menu_to_list()
        for dish in self.week_menu:
            qty = tk.StringVar()
            tk.Label(self, text=f'{dish[0]} - QTY:').pack()
            tk.Entry(self, textvariable=qty).pack()
            self.quantity.append(qty)

    def get_qty(self):
        return map((lambda var: var.get()), self.quantity)


class OrderRadio(tk.Frame):
    """
    The OrderRadio frame puts the orders into
    a radio button list, allowing us to view a specific
    client order through the order_id.
    """
    def __init__(self, master=None, side="top"):
        super().__init__(master)
        self.master = master
        self.orders = o.get_orders()
        self.vars = []
        self.var = tk.StringVar()
        for order in self.orders:
            tk.Radiobutton(self, indicatoron=0, text=f"{order.order_id}", variable=self.var, value=order.order_id, command=self.view_info).pack()
            self.vars.append(self.var)

    def view_info(self):
        return str(self.var.get())
