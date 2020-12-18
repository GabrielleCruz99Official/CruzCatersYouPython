from clients import client as c
from re import search
from debug import exceptions as e
import main
import logging as log

""" LOADING CLIENTS """


def load_client_list():
    """
    This function loads the lists of clients
    """
    c.load_clients("data\clientlist.txt")


def save_client_list():
    """
    This function saves the list of clients
    """
    c.save_clients("data\clientlist.txt")


def show_clients():
    """
    This function displays the clients using a generator
    """
    client_list = c.get_clients()
    for cl in client_list:
        yield cl.full_info().rstrip()


def add_client(name: str, surname: str, email: str, contact: str):
    """
    This function adds a new client to the database

    Precondition
    ------------
    - The name and surname must be unique
    - The name, surname, email, and contact number must have the type string

    Postcondition
    -------------
    - The client should now be added to the database
    - The client is ensured to have a unique ID
    - If any of the input values are missing, the function will raise
      an EmptyValue error
    """
    try:
        random_id = 0
        unique_id = False
        # this ensures the program will give a unique id to a client
        while not unique_id:
            random_id = c.random_id()
            if len([x for x in c.client_list if x.client_id == random_id]) == 0:
                unique_id = True
        c.client_list.append(c.Client(name, surname, email, contact, random_id))
    except e.EmptyValue:
        log.error("Incomplete values.")
    else:
        log.info("Client added.")


def remove_client(client_id: int):
    """
    This function deletes an existing client from the database

    Precondition
    ------------
    - The client must already exist
    - The input must be a client ID

    Postcondition
    -------------
    - The client should now be removed from the database
    - If the client ID is not an integer, the program will stop
    """
    try:
        c.client_list = [x for x in c.client_list if x.client_id != int(client_id)]
    except TypeError:
        log.error("That's not a valid ID.")
    except e.NotInDatabase:
        log.warning("You're trying to remove a client that doesn't exist.")
    else:
        log.info("Client removed.")


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
            old_client = input("Input the ID of the former client: ")
            remove_client(old_client)
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