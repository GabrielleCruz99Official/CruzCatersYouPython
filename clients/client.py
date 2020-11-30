class Client:
    """
    Initialize the client's contact details here

    Parameters
    ----------

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

    """
    Added a method returning a full name method to return a 
    string instance of the class so it can be written in a text file
    
    !!! will change or remove this method later !!!
    """
    def fullname(self):
        return f'{self.name} {self.surname}'

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)

    """
    __repr__ is used to return a tuple of the class instance
    """
    def __repr__(self):
        return 0



class ClientOrder(Client):
    def __init__(self, order_list=[], status="Wait"):
        self.order_list = order_list
        self.status = status


if __name__ == "__main__":
    me = Client("Gabrielle", "Cruz")
    print(me)
