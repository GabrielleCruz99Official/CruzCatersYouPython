import client as c

def load_client_list(filename):
    pass


def save_client_list(filename):
    pass


def show_clients():
    client_list = c.get_clients()
    for cl in client_list:
        yield cl


def load_clients():
    pass


def save_clients():
    pass


if __name__ == "__main__":
    test = show_clients()
    print(test)