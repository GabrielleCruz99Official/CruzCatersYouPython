class IDError(Exception):
    def __init__(self, dish_id="", message="Invalid ID!"):
        self.dish_id = dish_id
        self.message = message
        super().__init__(self.dish_id, self.message)

    def __str__(self):
        return f'{self.dish_id} -> {self.message}'


class AlreadyExists(Exception):
    pass


class EmptyValue(Exception):
    pass


class NotInDatabase(Exception):
    pass