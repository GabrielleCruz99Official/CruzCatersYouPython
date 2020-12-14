import tkinter as tk
from food import items as it
from food import setmenu as sm
from food import menu as m


class Menu(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Menu")
        self.geometry("600x600")
        self.create_widgets()

    def create_widgets(self):
        """TITLE FRAME"""
        self.title_frame = tk.Frame(self, borderwidth=2, relief='ridge')
        self.title_frame.pack(side="top")
        self.menu_label = tk.Label(self.title_frame, text="========\nMENU AND FOOD IDEAS\n========")
        self.menu_label.pack()
        # this is where we place our menu of the week
        self.week_menu = tk.Listbox(self.title_frame, width=0, height=0)
        self.week_menu.pack()
        # there is a button here to bind the loading of the menu text file
        # whenever the widgets are loaded
        self.display_menu = tk.Button(self.title_frame, text="Display Menu", fg="orange")
        self.display_menu.bind("<Button>", self.update_menu())
        self.display_menu.pack()

        """
        The two main components of this window - adding/removing dish ideas,
        and setting the menu of the week - are separated into their own
        window frames.
        """

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

        """
        There is an encasing frame for adding/removing dish ideas
        to make the interface look cleaner.
        """

        """FRAME FOR ADD/REMOVE DISHES"""
        self.change_idea_frame = tk.Frame(self.dish_frame, borderwidth=2, relief='ridge')
        self.change_idea_frame.pack()

        """FRAME FOR ADDING NEW DISHES"""
        self.add_dish_frame = tk.Frame(self.change_idea_frame, borderwidth=1, relief='ridge')
        self.add_dish_frame.pack(side="left")
        self.add_dish_frame_label = tk.Label(self.add_dish_frame, text="Add new dish?")
        self.add_dish_frame_label.pack()
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
        self.remove_dish_frame = tk.Frame(self.change_idea_frame, borderwidth=1, relief='ridge')
        self.remove_dish_frame.pack(side="right")
        self.remove_dish_frame_label = tk.Label(self.remove_dish_frame, text="Remove a dish?")
        self.remove_dish_frame_label.pack()
        self.remove_id_label = tk.Label(self.remove_dish_frame, text="Dish ID")
        self.remove_id_label.pack()
        self.remove_id = tk.Entry(self.remove_dish_frame)
        self.remove_id.pack()
        self.remove_new_dish = tk.Button(self.remove_dish_frame, text="Confirm")
        self.remove_new_dish.bind("<Button>", self.remove_dish)
        self.remove_new_dish.pack()

        """SET MENU"""
        self.set_menu_frame = tk.Frame(self, borderwidth=2, relief='ridge')
        self.set_menu_frame.pack(side="right")
        self.menu_ideas = tk.Frame(self.set_menu_frame, borderwidth=1, relief='ridge')
        self.menu_ideas.pack()
        self.dish_ideas = Checkbar(self.menu_ideas)
        self.dish_ideas.pack()
        self.new_menu = tk.Button(self.set_menu_frame, text="Confirm New Menu")
        self.new_menu.bind("<Button>", self.set_menu)
        self.new_menu.pack()

        """RETURN TO MAIN MENU"""
        # This button will hide the window and return to the main menu
        self.menu_back = tk.Button(self, text="Return", fg="red", width=0, height=0)
        self.menu_back.bind('<Button>', self.go_back)
        self.menu_back.pack(side="bottom")

    """
    These functions are calling the backend methods in their own way
    for the GUI to interact with the backend and the database.
    """

    def add_dish(self, event):
        it.add_item(self.add_id.get(), self.add_name.get(), int(self.add_price.get()))
        self.update_dishes()

    def remove_dish(self, event):
        it.remove_item(self.remove_id.get())
        self.update_dishes()

    def set_menu(self, event):
        toggle = list(self.dish_ideas.selected())
        sm.clear_menu()
        dish_ideas = it.food_idea_to_list()
        for dish in dish_ideas:
            index = dish_ideas.index(dish)
            if toggle[index] == 1:
                sm.add_menu_dish(dish[1]['name'], dish[1]['price'])
        self.update_menu()

    """
    These next two are responsible for updating the menu of the week
    and dish ideas in the interface
    """

    def update_menu(self):
        self.week_menu.delete(0, tk.END)
        wm = sm.weekly_menu_to_list()
        for menu_dish in wm:
            self.week_menu.insert(wm.index(menu_dish), f'{menu_dish[0]}: {menu_dish[1]}')

    def update_dishes(self):
        self.dish_box.delete(0, tk.END)
        di = it.food_idea_to_list()
        for dish in di:
            self.dish_box.insert(di.index(dish), '{}- {}: {}'.format(dish[0], dish[1]['name'], dish[1]['price']))

    # This will hide the menu window
    def go_back(self, event):
        m.save_dish()
        m.save_menu()
        self.withdraw()
        print("Back to main menu.")


class Checkbar(tk.Frame):
    """
    The Checkbar frame puts the dish ideas into
    a checkbox list, allowing us to pick which
    dishes we want to serve this week.
    """
    def __init__(self, master=None, side="top"):
        super().__init__(master)
        self.master = master
        self.text = tk.Label(self, text="-New Menu-")
        self.text.pack()
        self.vars = []
        # we are getting the list of food ideas
        # and giving each dish a checkbox
        self.dishes = it.food_idea_to_list()
        for dish in self.dishes:
            var = tk.IntVar()
            chk = tk.Checkbutton(self, text='{}: {}'.format(dish[1]['name'], dish[1]['price']), variable=var)
            chk.pack(side=side)
            self.vars.append(var)

    # This returns a "list" of 0 and 1 values that
    # determines if the dish was selected for this week
    def selected(self):
        return map((lambda var: var.get()), self.vars)