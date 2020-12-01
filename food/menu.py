from food import items
"""
This module imports the list of food items
and allows the user to create a menu from
that list
"""
test_list = items.food_menu_to_list()
menu = []

def display_dishes():
    print("==========\nDISH IDEAS\n==========")
    for item in test_list:
        print(item)
        # menu.append([id, info] for id, info in item)

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