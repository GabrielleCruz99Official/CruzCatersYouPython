import unittest as test
from food import setmenu as sm


class TestAddDishToMenu(test.TestCase):
    def test_add_dish_to_menu_success(self):
        sm.week_menu = {}
        sm.add_menu_dish('Beef Kare-Kare', 12)
        actual = sm.week_menu
        expected = {'Beef Kare-Kare': 12}
        self.assertDictEqual(actual, expected)


class TestClearMenu(test.TestCase):
    def test_clear_menu_success(self):
        sm.week_menu = {'Test1': 10, 'Test2': 11, 'Test3': 12}
        sm.clear_menu()
        actual = sm.week_menu
        expected = {}
        self.assertDictEqual(actual, expected)


class TestDictToList(test.TestCase):
    def test_dict_to_list_success(self):
        sm.week_menu = {'Test1': 10, 'Test2': 11, 'Test3': 12}
        actual = sm.weekly_menu_to_list()
        expected = [('Test1', 10), ('Test2', 11), ('Test3',12)]
        self.assertListEqual(actual, expected)


if __name__ == "__main__":
    test.main()