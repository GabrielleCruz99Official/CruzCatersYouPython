# initialize list of clients
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

    """
    These next few functions will be important because they unify
    class instance values for later unpacking
    """

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


""" CLIENT FUNCTIONS """


def get_clients():
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
    Target file must exist.

    Postcondition
    -------------
    The client_list will be filled with values
    loaded from the file.

    Raises
    ------
    -FileNotFoundError if file does not exist
    -ValueError if the line has too many values to unpack
    -IOError if a problem in I/O arises
    """
    try:
        with open(filename, "r") as file:
            for line in file:
                full_name, email, contact = line.split(", ")
                name, surname = full_name.split(" ")
                client_list.append(Client(name, surname, email, contact))
    except FileNotFoundError as f:
        print(f)
    except ValueError as v:
        print(v)
    except IOError as io:
        print(io)
    except Exception as e:
        print(e)
    else:
        print("File loaded.")


def save_clients(filename: str):
    """
    This will save the list of clients into
    a text file
    :param filename:
    :type filename: str

    Precondition
    ------------
    Target file must exist. If not, the program will create one.

    Postcondition
    -------------
    The file will contain the list of clients

    Raises
    ------
    IOError if there is a problem in I/O

    """
    try:
        with open(filename, "w") as file:
            for client in client_list:
                temp_str = f'{client.full_info()}'
                file.writelines(f'{temp_str.rstrip()}\n')
    except IOError as io:
        print(io)
    except Exception as e:
        print(e)
    else:
        print("List saved to database.")


if __name__ == "__main__":
    load_clients("clientlist.txt")
    print(client_list)
