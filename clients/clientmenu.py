from clients import client as c
from re import search
import main

""" LOADING CLIENTS """


def load_client_list():
    c.load_clients("data\clientlist.txt")


def save_client_list():
    c.save_clients("data\clientlist.txt")


def show_clients():
    """
    This function displays the clients using a generator
    """
    client_list = c.get_clients()
    for cl in client_list:
        yield cl.full_info().rstrip()


def add_client(name: str, surname: str, email: str, contact: str):
    c.client_list.append(c.Client(name, surname, email, contact))


def remove_client(name: str, surname: str):
    c.client_list = [x for x in c.client_list if x.name != name and x.surname != surname]


""" CONSOLE MESSAGES """


def display_clients_interface():
    c.client_list = []
    load_client_list()
    print("""=======\nCLIENTS\n=======""")
    client_option = input("1: View Clients\n2: Add Client\n3: Remove Client\nType anything else to return: ")
    if search("[0-9]", client_option):
        if client_option == "1":
            for cl in show_clients():
                print(cl)
        if client_option == "2":
            new_client = input("Input details in this format\n(Name, Surname, Email, Contact Number): ")
            name, surname, email, contact = new_client.split(", ")
            add_client(name, surname, email, contact)
            print("Client added")
            save_client_list()
        if client_option == "3":
            old_client = input("Input the details of the former client\nFormat(Name, Surname): ")
            name, surname = old_client.split(", ")
            remove_client(name, surname)
            print("Client removed")
            save_client_list()
        display_clients_interface()
    else:
        main.intro_message()



if __name__ == "__main__":
    try:
        c.load_clients("clientlist.txt")
        for cli in show_clients():
            print(cli)

    except Exception as e:
        print(e)