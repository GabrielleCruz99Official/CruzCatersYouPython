import client as c


def show_clients():
    """
    This function
    :return:
    """
    client_list = c.get_clients()
    for cl in client_list:
        yield cl


if __name__ == "__main__":
    for client in show_clients():
        print(client)