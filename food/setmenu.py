# week menu: name, price
week_menu = {}


def load_menu_file(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                name, price = line.rstrip().split(", ")
    except Exception as e:
        print(e)


def save_menu_file(filename):
    try:
        with open(filename, "w") as file:
            for dish in week_menu:
                name, price = dish, week_menu[dish]
                file.writelines(f"{name}, {price}\n")
    except Exception as e:
        print(e)


def add_menu_dish(name, price):
    if name not in week_menu:
        week_menu[name] = price
    else:
        print("Item already added to weekly menu!")


def remove_menu_dish(name):
    if name in week_menu:
        del (week_menu[name])
    else:
        print("Item not in weekly menu!")


def weekly_menu_to_list():
    return [(name, price) for name, price in week_menu.items()]


if __name__ == "__main__":
    week_menu = {"Test1": 12, "Test2": 10, "Test3": 8}
    save_menu_file("weeklymenu.txt")
    load_menu_file("weeklymenu.txt")
    week_test_menu = weekly_menu_to_list()
    print(week_test_menu)
