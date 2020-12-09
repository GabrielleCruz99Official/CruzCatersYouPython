import client as c


class ClientOrder(c.Client):
    def __init__(self, menu_order=[], subtotal=0, status="Wait"):
        self._menu_order = menu_order
        self._subtotal = subtotal
        self._status = status

    @property
    def menu_order(self):
        return self._menu_order

    @menu_order.setter
    def menu_order(self, menu_order):
        self.menu_order = menu_order

    @property
    def subtotal(self):
        return self._subtotal

    @subtotal.setter
    def subtotal(self, subtotal):
        self.subtotal = subtotal

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self.status = status



