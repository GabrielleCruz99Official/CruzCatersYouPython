from debug import exceptions as exc
import logging as log
# set up empty dictionary
menu_idea = {}


def load_dish_file(filename: str):
    """
    This will load all the dish ideas into the application.

    :param filename: file that contains all dish ideas
    :type filename: str

    Precondition
    ------------
    The target file exists and contains values.

    Postcondition
    -------------
    The menu_idea dictionary will be filled with
    potential dishes for a weekly menu.

    """
    try:
        with open(filename, "r") as file:
            for line in file:
                temp_id, temp_name, temp_price = line.split(", ")
                add_item(temp_id, temp_name, int(temp_price))
    except FileNotFoundError:
        log.error("Dishes file not found!")
    except IOError:
        log.error("Unable to load file.")
    else:
        log.info("Dishes file loaded.")


def save_dish_file(filename: str):
    """
    This will save all current potential dishes in a
    file (serving as a temporary database).

    :param filename: file that contains all dish ideas
    :type filename: str

    Precondition
    ------------
    The target file exists.

    Postcondition
    -------------
    The target file will contain the various dishes
    the user has inputted or updated. If the file didn't exist,
    the program will create a file with the inputted name and
    input the dish ideas into it.
    """
    try:
        with open(filename, "w") as file:
            temp_dish = food_idea_to_list()
            for dish in temp_dish:
                temp_id, temp_info = dish
                temp_name, temp_price = temp_info.values()
                file.writelines(f"{temp_id}, {temp_name}, {temp_price}\n")
    except FileNotFoundError:
        log.error("Dishes file not found! The program will create a file.")
    except IOError:
        log.error("Unable to save data.")
    else:
        log.info("Dishes saved to database.")


def add_item(dish_id: str, dish_name: str, dish_price: int):
    """
    This method allows the user to add a new food item to
    the list of menu ideas

    :param dish_id: The dish ID
    :type dish_id: str

    :param dish_name: The name of the new dish idea
    :type dish_name: str

    :param dish_price: The price of the new dish idea
    :type dish_price: int

    Preconditions
    -------------
    - The length of item_id must be exactly 3
    - The price number must be an integer
    - The inputted value of dish_id must not already exist
    - All the values must be filled

    Postcondition
    -------------
    - The dish inputted is added to the ideas

    Raises
    ------
    - ID Error: if the dish ID does not have exactly 3 letters
    - TypeError: if the price inputted is not an integer
    """
    try:
        if dish_id not in menu_idea:
            menu_idea[dish_id] = {"name": dish_name, "price": dish_price}
        else:
            log.warning("Dish already exists!")
    except exc.IDError:
        log.error("You need to input only 3 letters for the ID")
    except TypeError:
        log.error("The price you inputted is not a number!")
    else:
        log.info("Dish added!")


def remove_item(dish_id: str):
    """
    This method allows the user to delete an existing food item
    to the list of menu ideas
    :param dish_id: string
    :return: the function does not return anything as
    we are only deleting an item to the list

    Precondition:
    - The length of dish_id must be exactly 3

    Postcondition:
    - The target dish is removed from the ideas

    Raises:
    - ID Error: if the dish ID does not have exactly 3 letters
    - KeyError: if the key doesn't exist in the database
    """
    try:
        del (menu_idea[dish_id])
    except exc.IDError:
        log.error("You need to input only 3 letters for the ID")
    except KeyError:
        log.error("Dish doesn't exist in the database")
    else:
        log.info("Dish removed!")


def food_idea_to_list() -> list:
    """
    This function converts the dictionary
    into a list to be viewed by the interface
    :return: converted list of dish ideas
    """
    return [(food_item, food_info) for food_item, food_info in menu_idea.items()]


if __name__ == "__main__":
    try:
        load_dish_file("dishes.txt")
        test_dish = food_idea_to_list()
        save_dish_file("dishes.txt")
    except Exception as e:
        print(e)
