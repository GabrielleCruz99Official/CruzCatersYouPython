from food import items
"""
This module imports the list of food items
and allows the user to create a menu from
that list
"""
def load_dish_list():
    test_list = items.food_menu_to_list()
    for dish in test_list:
        print(dish)

def display_dishes():
    print("\n==========\nDISH IDEAS\n==========")
    load_dish_list()
    change_dish = input("Would you like to edit the list of dishes?\nY/N - Input here: ")
    if change_dish.lower() == "yes" or change_dish.lower() == "y":
        action = input(
            "What would you like to do?\n1: Add a dish to list\n2: Remove a dish from the list\n3: Go back\n=>")
        if action == "1":
            dish_id, dish_name, dish_price = input(
                "To add a dish, please use this format:\nDDD(for dish_id), name, price\n=> ").split(", ")
            print(dish_id, dish_name, dish_price)
            items.add_item(dish_id, dish_name, dish_price)
            print("Dish added to list!")
            display_dishes()
        elif action == "2":
            dish_id = input("Please input the 3-letter code of the dish you wish to remove: ")
            items.remove_item(dish_id)
            print("Dish")
            display_dishes()
        else:
            display_interface()
    else:
        save_dishes()
        display_interface()


def display_interface():
    print("\n================\nMENU OF THE WEEK\n================")
    print("1: Display Dishes\n2: Set Menu\n3: Display Menu of the Week")
    main_input = input("What do you want to do? ")
    if main_input == "1": display_dishes()
    else:
        save_state()
        print("See you soon!")

def save_dishes():
    try:
        pass
    except:

def save_state():
    """
    This function is called every time you close the app.
    It will save the current list of dish ideas, the menu of the week,
    and the clients' orders.
    """
    return 0

if __name__ == "__main__":
    try:
        display_interface()
        """
        Insert here a display menu that will ask user input
        to save menu
        """

    except Exception as e:
        print(e)