client_list = []


class Client:
    """
    Initialize the client's contact details here
    """
    def __init__(self, name="", surname="", email="", contact_number=""):
        self._name = name
        self._surname = surname
        self._email = email
        self._contact_number = contact_number

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

    def info(self):
        return f'{self.email}, {self.contact_number}'

    """
    __repr__ is used to return a tuple of the class instance
    """
    def __repr__(self):
        return '{} {}'.format(self.name, self.surname)


def get_clients():
    """
    returns the list of clients in the database
    :return: client_list: list
    """
    return client_list


def load_clients(filename):
    pass


def save_clients(filename):
    pass


client_list.append(Client("Gabrielle", "Cruz", "test@gmail.com", "0487362360"))
client_list.append(Client("Christian", "Cruz", "test2@gmail.com", "0471935165"))


if __name__ == "__main__":
    client_list.append(Client("Gabrielle", "Cruz", "test@gmail.com", "0487362360"))
    client_list.append(Client("Christian", "Cruz", "test2@gmail.com", "0471935165"))
    print(client_list)
