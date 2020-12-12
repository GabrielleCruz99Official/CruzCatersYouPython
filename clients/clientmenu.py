from clients import client as c


""" LOADING CLIENTS """


def show_clients():
    """
    This function displays the clients using a generator
    """
    client_list = c.get_clients()
    for cl in client_list:
        yield cl.full_info().rstrip()


def add_client(name: str, surname: str, email: str, contact: str):
    c.client_list.append(c.Client(name, surname, email, contact))


""" CONSOLE MESSAGES """


def display_clients_interface():
    pass


if __name__ == "__main__":
    try:
        c.load_clients("clientlist.txt")

        for cli in show_clients():
            print(cli)

    except Exception as e:
        print(e)