menu_idea_list = {
    "BKK": {
        "name": "Beef Kare-Kare",
        "price": 12
    },
    "CPS": {
        "name": "Chicken Pasta Salad",
        "price": 6
    },
    "LCF": {
        "name": "Leche Flan",
        "price": 6
    },
    "CHS": {
        "name": "Creamy Cheesecake",
        "price": 15
    }
}

def add_item(item_id, item_name, item_price):
    """
    This method allows the user to add a new food item to
    the list of menu ideas
    :param item_id: string
    :param item_name: string
    :param item_price: int
    :return: the function does not return anything as
    we are only adding an item to the list

    Preconditions:
    - The length of item_id must be exactly 3
    """
    menu_idea_list[item_id] = {"name": item_name, "price": item_price}

def remove_item(item_id):
    """
    This method allows the user to delete an existing food item
    to the list of menu ideas
    :param item_id: string
    :return: the function does not return anything as
    we are only deleting an item to the list

    Preconditions:
    - The length of item_id must be exactly 3
    """
    del(menu_idea_list[item_id])

def food_menu_to_list():
    return [(food_item, food_info) for food_item, food_info in menu_idea_list.items()]

if __name__ == "__main__":
    add_item("TST", "test", 10)
    print(menu_idea_list)
    remove_item("TST")
    print(menu_idea_list)
    test_list = food_menu_to_list()
    print(test_list)
