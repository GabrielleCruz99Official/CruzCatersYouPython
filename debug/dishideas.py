import unittest as test
from debug import exceptions as exc
from food import items as it

"""
Here, we will find the application quality control tests
in case we encounter bugs
"""


class TestAddDishToIdea(test.TestCase):
    def test_add_dish_success(self):
        it.menu_idea = {}
        it.add_item('TST', 'Test', 10)
        actual = it.menu_idea
        expected = {'TST': {'name': 'Test', 'price': 10}}
        self.assertDictEqual(actual, expected)

    def test_bad_id(self):
        with self.assertRaises(exc.IDError):
            it.add_item('TSTAN', 'Testan', 10)


class TestRemoveDish(test.TestCase):
    def test_remove_dish_success(self):
        it.menu_idea = {'TSA': {'name': 'TestOne', 'price': 1}, 'TSB': {'name': 'TestTwo', 'price': 2}}
        it.remove_item('TSB')
        actual = it.menu_idea
        expected = {'TSA': {'name': 'TestOne', 'price': 1}}
        self.assertDictEqual(actual, expected)


class TestDictToList(test.TestCase):
    def test_dict_to_list_success(self):
        it.menu_idea = {'TSA': {'name': 'TestOne', 'price': 1}, 'TSB': {'name': 'TestTwo', 'price': 2}}
        actual = it.food_idea_to_list()
        expected = [('TSA', {'name': 'TestOne', 'price': 1}), ('TSB', {'name': 'TestTwo', 'price': 2})]
        self.assertListEqual(actual, expected)


if __name__ == "__main__":
    test.main()