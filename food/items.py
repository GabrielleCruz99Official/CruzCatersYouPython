# set up empty dictionary
menu_idea = {}


def load_dish_file(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                temp_id, temp_name, temp_price = line.split(", ")
                add_item(temp_id, temp_name, temp_price)
    except Exception as e:
        print(e)


def save_dish_file(filename):
    try:
        with open(filename, "w") as file:
            temp_dish = food_idea_to_list()
            for dish in temp_dish:
                temp_id, temp_info = dish
                temp_name, temp_price = temp_info.values()
                file.writelines(f"{temp_id}, {temp_name}, {temp_price}")
    except Exception as e:
        print(e)


def add_item(dish_id, dish_name, dish_price):
    """
    This method allows the user to add a new food item to
    the list of menu ideas
    :param dish_id: string
    :param dish_name: string
    :param dish_price: int
    :return: the function does not return anything as
    we are only adding an item to the list

    Preconditions:
    - The length of item_id must be exactly 3
    """
    if dish_id not in menu_idea:
        menu_idea[dish_id] = {"name": dish_name, "price": dish_price}


def remove_item(dish_id):
    """
    This method allows the user to delete an existing food item
    to the list of menu ideas
    :param dish_id: string
    :return: the function does not return anything as
    we are only deleting an item to the list

    Preconditions:
    - The length of item_id must be exactly 3
    """
    if dish_id in menu_idea:
        del (menu_idea[dish_id])


def food_idea_to_list():
    return [(food_item, food_info) for food_item, food_info in menu_idea.items()]


if __name__ == "__main__":
    load_dish_file("dishes.txt")
    test_dish = food_idea_to_list()
    save_dish_file("dishes.txt")
