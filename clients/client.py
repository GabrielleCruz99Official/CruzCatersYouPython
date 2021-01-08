from random import randint as rand
import logging as log

# initialize list of clients
client_list = []


class Client:
    """
    Initialize the client's contact details here
    """
    def __init__(self, name="", surname="", email="", contact_number="", client_id=0):
        self._name = name
        self._surname = surname
        self._email = email
        self._contact_number = contact_number
        self._client_id = client_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self.surname = surname

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self.email = email

    @property
    def contact_number(self):
        return self._contact_number

    @contact_number.setter
    def contact_number(self, contact_number):
        self.contact_number = contact_number

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        self.client_id = client_id

    """
    These next few functions will be important because they unify
    class instance values for later unpacking
    """

    def full_name(self):
        return f'{self.name} {self.surname}'

    def contact_info(self):
        return f'{self.email}, {self.contact_number}'

    def full_info(self):
        return f'{self.full_name()}, {self.contact_info()}, {self.client_id}'

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)

    def __del__(self):
        pass


""" CLIENT FUNCTIONS """


def random_id() -> int:
    """
    This is the random id generator for each new order
    :return: a random integer between 100000 and 999999
    """
    return rand(100000, 999999)


def get_clients() -> list:
    """
    returns the list of clients in the database
    :return: client_list

    Precondition
    ------------
    The client_list must exist and has values
    """
    return client_list


def load_clients(filename: str):
    """
    This will load the clients from a text file
    into a list
    :param filename:
    :type filename: str

    Precondition
    ------------
    The file to be loaded must exist.

    Postcondition
    -------------
    The client list will be filled with values
    loaded from the file.

    Raises
    ------
    -FileNotFoundError if file does not exist
    -IOError if a problem in I/O arises
    """
    with open(filename, "r") as file:
        for line in file:
            full_name, email, contact, client_id = line.split(", ")
            name, surname = full_name.split(" ")
            client_list.append(Client(name, surname, email, contact, int(client_id)))
        log.info("Client list loaded.")


def save_clients(filename: str):
    """
    This will save the list of clients into
    a text file
    :param filename:
    :type filename: str

    Precondition
    ------------
    Target file must exist.

    Postcondition
    -------------
    The file will contain the list of clients. If the file didn't
    exist before, the program will create one and input the data
    in that file.

    Raises
    ------
    IOError if there is a problem in I/O

    """
    with open(filename, "w") as file:
        for cl in client_list:
            temp_str = f'{cl.full_info()}'
            file.writelines(f'{temp_str.rstrip()}\n')
        log.info("Clients saved to database.")


if __name__ == "__main__":
    load_clients(".\..\data\clientlist.txt")
    for client in client_list:
        print(client.client_id)
