import tkinter as tk


class Orders(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Orders")
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
        self.withdraw()