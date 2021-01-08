import unittest as test
from debug import exceptions as exc
from food import items as it

"""
Here, we will find the application quality control tests
for the dish ideas module in case we encounter bugs
"""


class TestAddDishToIdea(test.TestCase):
    def test_add_dish_success(self):
        it.menu_idea = {}
        it.add_item('TST', 'Test', 10)
        it.add_item('P-O', 'post', 11)
        actual = it.menu_idea
        expected = {'TST': {'name': 'Test', 'price': 10}, 'P-O': {'name': 'post', 'price': 11}}
        self.assertDictEqual(actual, expected)

    def test_dish_already_in_list(self):
        it.menu_idea = {'MMM': {'name': 'Me', 'price': 10}, 'YYY': {'name': 'You', 'price': 12}}
        self.assertRaises(KeyError, it.add_item, 'YYY', 'Yes', 12)

    def test_bad_id(self):
        with self.assertRaises(exc.IDError):
            it.add_item('TSTAN', 'Testan', 10)

    def test_int_for_price(self):
        with self.assertRaises(TypeError):
            it.add_item('TST', 'Test', 'LOL')


class TestRemoveDish(test.TestCase):
    def test_remove_dish_success(self):
        it.menu_idea = {'TSA': {'name': 'TestOne', 'price': 1}, 'TSB': {'name': 'TestTwo', 'price': 2}}
        it.remove_item('TSB')
        actual = it.menu_idea
        expected = {'TSA': {'name': 'TestOne', 'price': 1}}
        self.assertDictEqual(actual, expected)

    def test_dish_not_in_ideas(self):
        it.menu_idea = {'TSA': {'name': 'TestOne', 'price': 1}, 'TSB': {'name': 'TestTwo', 'price': 2}}
        self.assertRaises(KeyError, it.remove_item, 'TSC')

    def test_bad_id(self):
        it.menu_idea = {'TSA': {'name': 'TestOne', 'price': 1}, 'TSB': {'name': 'TestTwo', 'price': 2}}
        with self.assertRaises(exc.IDError):
            it.remove_item('TSTAN')


class TestDictToList(test.TestCase):
    def test_dict_to_list_success(self):
        it.menu_idea = {'TSA': {'name': 'TestOne', 'price': 1}, 'TSB': {'name': 'TestTwo', 'price': 2}}
        actual = it.food_idea_to_list()
        expected = [('TSA', {'name': 'TestOne', 'price': 1}), ('TSB', {'name': 'TestTwo', 'price': 2})]
        self.assertListEqual(actual, expected)


if __name__ == "__main__":
    test.main()