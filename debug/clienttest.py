from clients import clientmenu as cm
from clients import client as c
import unittest as test


class TestAddClient(test.TestCase):
    def setUp(self):
        super(TestAddClient, self).setUp()
        self.addTypeEqualityFunc(str, self.assertMultiLineEqual)
        
    def test_add_client_success(self):
        c.client_list = []
        cm.add_client('Gabe', 'Cruz', 'test@gmail.com', '0487362360')
        actual = c.client_list[0].full_info()
        expected = 'Gabe Cruz, test@gmail.com, 0487362360'
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            expected2 = 'Test One, test.com, 0004'
            self.assertEqual(actual, expected2)


class TestRemoveClient(test.TestCase):
    def setUp(self):
        super(TestRemoveClient, self).setUp()
        self.addTypeEqualityFunc(str, self.assertMultiLineEqual)

    def test_remove_client_success(self):
        c.client_list = []



if __name__ == "__main__":
    test.main()