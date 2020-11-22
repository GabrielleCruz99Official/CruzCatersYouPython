class Client:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    @property
    def full_name(self):
        return 'f{self._name} {self._surname}'

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

    def __str__(self):
        return f'The client is {self.name} {self.surname}'


class ClientOrder(Client):
    def __init__(self, order_list=[], status="Wait"):
        self.order_list = order_list
        self.status = status


if __name__ == "__main__":
    print("Hello world")
    me = Client("Gabrielle", "Cruz")
    print(me)
