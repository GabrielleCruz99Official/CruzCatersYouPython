from food import items
import re
"""
This module imports the list of food items
and allows the user to create a menu from
that list
"""
test_list = items.food_menu_to_list()
menu = []

def display_dishes():
    print("==========\nDISH IDEAS\n==========")
    for dish in test_list:
        print(dish)
    change_dish = input("Would you like to edit the list of dishes?\nY/N - Input here: ")
    if len(change_dish) > 3 or change_dish.lower() == "no" or change_dish.lower == "n":
        display_interface()
    else:
        action = input("What would you like to do?\n1: Add a dish to list\n2: Remove a dish from the list\n3: Go back")
        if action == "1":
            dish_id, dish_name, dish_price = input("To add a dish, please use this format:\nDDD(for dish_id), name, price").split(",")
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

def display_interface():
    print("================\nMENU OF THE WEEK\n================")
    print("1: Display Dishes\n2: Set Menu\n3: Display Menu of the Week")
    main_input = input("What do you want to do? ")
    display_dishes() if main_input == "1" else print("Function not done!")

if __name__ == "__main__":
    try:
        display_interface()
        """
        Insert here a display menu that will ask user input
        to save menu
        """

    except Exception as e:
        print(e)