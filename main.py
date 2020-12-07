from food import menu


def load_main_menu():
    """
    This function displays the application's main menu.
    """
    intro_message()


def intro_message():
    print("\n=============\nCRUZCATERSYOU\n=============")
    mode_select = input("Select mode:\n1: Menu\n2: Clients\n3: Orders\nType anything else to exit: ")
    if mode_select == "1":
        menu.display_interface()
    if mode_select == "2":
        pass
    else:
        print("Goodbye!")


if __name__ == "__main__":
    try:
        load_main_menu()
    except Exception as e:
        print(e)
