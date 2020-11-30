from itemlist import items
"""
This module imports the list of food items
and allows the user to create a menu from
that list
"""
test_list = items.menu_idea_list
menu = []

for key in test_list:
    menu.append(test_list[key])
if __name__ == "__main__":
    try:
        print(menu)
        """
        Insert here a display menu that will ask user input
        to save menu
        """

    except Exception as e:
        print(e)