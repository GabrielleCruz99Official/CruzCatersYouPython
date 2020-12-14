import tkinter as tk
from clients import client as c
from clients import clientmenu as cm


class Clients(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Clients")
        self.geometry("300x450")
        self.create_widgets()

    def create_widgets(self):
        self.client_label = tk.Label(self, text="=======\nCLIENTS\n=======")
        self.client_label.pack()

        """CLIENTS FRAME"""
        self.client_frame = tk.Frame(self, borderwidth=2, relief='ridge')
        self.client_frame.pack(side="top")
        self.client_list_label = tk.Label(self.client_frame, text="-Client List-")
        self.client_list_label.pack()

        self.client_list = Radiobar(self.client_frame)
        self.client_list.pack(side="left")

        self.view_client = tk.Button(self.client_list, text="Display Client")
        self.view_client.bind("<Button>", self.display_client)
        self.view_client.pack(side="bottom")

        self.client_info = tk.Listbox(self.client_frame, width=0, height=0)
        self.client_info.pack(side="right")

        """ADD/REMOVE CLIENTS FRAME"""
        self.change_client_list = tk.Frame(self, borderwidth=2, relief='ridge')
        self.change_client_list.pack(side="top")
        self.change_client_label = tk.Label(self.change_client_list, text="-Add or Remove a Client-")
        self.change_client_label.pack(side="top")

        """ADD CLIENTS"""
        self.add_client = tk.Frame(self, borderwidth=1, relief='ridge')
        self.add_client.pack(side="left")

        self.add_client_label = tk.Label(self.add_client, text="Add New Client")
        self.add_client_label.pack(side="top")

        self.add_name_label = tk.Label(self.add_client, text="Name")
        self.add_name_label.pack()
        self.add_client_name = tk.Entry(self.add_client)
        self.add_client_name.pack()

        self.add_surname_label = tk.Label(self.add_client, text="Surname")
        self.add_surname_label.pack()
        self.add_client_surname = tk.Entry(self.add_client)
        self.add_client_surname.pack()

        self.add_email_label = tk.Label(self.add_client, text="Email")
        self.add_email_label.pack()
        self.add_client_email = tk.Entry(self.add_client)
        self.add_client_email.pack()

        self.add_contact_label = tk.Label(self.add_client, text="Contact Number")
        self.add_contact_label.pack()
        self.add_client_contact = tk.Entry(self.add_client)
        self.add_client_contact.pack()

        self.add_client_confirm = tk.Button(self.add_client, text="Confirm")
        self.add_client_confirm.bind("<Button>", self.add_new_client)
        self.add_client_confirm.pack(side="bottom")

        """REMOVE CLIENTS"""

        self.remove_client = tk.Frame(self, borderwidth=1, relief='ridge')
        self.remove_client.pack(side="right")

        self.remove_client_label = tk.Label(self.remove_client, text="Remove a Client")
        self.remove_client_label.pack(side="top")

        self.remove_name_label = tk.Label(self.remove_client, text="Name")
        self.remove_name_label.pack()
        self.remove_client_name = tk.Entry(self.remove_client)
        self.remove_client_name.pack()

        self.remove_surname_label = tk.Label(self.remove_client, text="Surname")
        self.remove_surname_label.pack()
        self.remove_client_surname = tk.Entry(self.remove_client)
        self.remove_client_surname.pack()

        self.remove_client_confirm = tk.Button(self.remove_client, text="Confirm")
        self.remove_client_confirm.bind("<Button>", self.remove_old_client)
        self.remove_client_confirm.pack(side="bottom")

        """RETURN TO MAIN MENU"""

        self.client_back = tk.Button(self, text="Return", fg="red")
        self.client_back.bind('<Button>', self.go_back)
        self.client_back.pack()

    def display_client(self, event):
        self.client_info.delete(0, tk.END)
        info = self.client_list.view_info()
        full_name, email, contact = info.split(", ")
        temp_text_1 = 'Name: {}'.format(full_name)
        temp_text_2 = 'Email: {}'.format(email)
        temp_text_3 = 'Contact Info: {}'.format(contact)
        self.client_info.insert(0, temp_text_1)
        self.client_info.insert(1, temp_text_2)
        self.client_info.insert(2, temp_text_3)

    def add_new_client(self, event):
        cm.add_client(self.add_client_name.get(), self.add_client_surname.get(), self.add_client_email.get(), self.add_client_contact.get())

    def remove_old_client(self, event):
        name = self.remove_client_name.get()
        surname = self.remove_client_surname.get()
        cm.remove_client(name, surname)

    def go_back(self, event):
        print("Back to main menu.")
        cm.save_client_list()
        self.withdraw()


class Radiobar(tk.Frame):
    """
    The Radiobar frame puts the clients into
    a radio button list, allowing us to view
    each client's information
    """
    def __init__(self, master=None, side="top"):
        super().__init__(master)
        self.master = master
        self.clients = c.get_clients()
        self.vars = []
        self.var = tk.StringVar()
        for client in self.clients:
            tk.Radiobutton(self, indicatoron=0, text=f"{client.full_name()}", variable=self.var, value=client.full_info(), command=self.view_info).pack()
            self.vars.append(self.var)

    def view_info(self):
        return str(self.var.get())