# week menu: name, price
week_menu = {}


def load_menu_file(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                name, price = line.rstrip().split(", ")
                add_menu_dish(name, price)
    except Exception as e:
        print(e)


def save_menu_file(filename):
    try:
        with open(filename, "w") as file:
            for dish in week_menu:
                name, price = dish, week_menu[dish]
                file.writelines(f"{name}, {price}")
    except Exception as e:
        print(e)


def add_menu_dish(name, price):
    if name not in week_menu:
        week_menu[name] = price


def clear_menu():
    week_menu.clear()


def weekly_menu_to_list():
    return [(name, price) for name, price in week_menu.items()]


if __name__ == "__main__":
    week_menu = {"Test1": 12, "Test2": 10, "Test3": 8}
    save_menu_file("weeklymenu.txt")
    load_menu_file("weeklymenu.txt")
    week_test_menu = weekly_menu_to_list()
    print(week_test_menu)
