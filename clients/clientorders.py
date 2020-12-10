import client as c
from food import setmenu as menu

""" CLIENT ORDERS """
client_orders = []


class ClientOrder(c.Client):
    def __init__(self, name="", surname="", email="", contact_number = "", order_list=[], subtotal=0, status="WAIT"):
        super().__init__(name, surname, email, contact_number)
        self._order_list = order_list
        self._subtotal = subtotal
        self._status = status

        


""" LOADING AND SAVING ORDERS """


def get_orders():
    """
    returns the list of clients in the database
    :return: client_list: list
    """
    return client_orders


if __name__ == "__main__":
    test = c.Client("Test", "Toot")
    test_order = ClientOrder(test)
    print(test_order.full_name())
