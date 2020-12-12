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

    def full_name(self):
        return f'{self.name} {self.surname}'

    def contact_info(self):
        return f'{self.email}, {self.contact_number}'

    def full_info(self):
        return f'{self.full_name()}, {self.contact_info()}'

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)

    def __del__(self):
        pass


def get_clients():
    """
    returns the list of clients in the database
    :return: client_list
    """
    return client_list


def load_clients(filename: str):
    try:
        with open(filename, "r") as file:
            for line in file:
                full_name, email, contact = line.split(", ")
                name, surname = full_name.split(" ")
                client_list.append(Client(name, surname, email, contact))
    except Exception as e:
        print(e)


def save_clients(filename: str):
    try:
        with open(filename, "w") as file:
            for client in client_list:
                temp_str = f'{client.full_info()}'
                file.writelines(f'{temp_str}\n')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    load_clients("clientlist.txt")
    print(client_list)
