from clients import clientmenu as cm
from clients import client as c
from debug import exceptions as e
import unittest as test


class TestAddClient(test.TestCase):
    def setUp(self):
        super(TestAddClient, self).setUp()
        self.addTypeEqualityFunc(str, self.assertMultiLineEqual)
        
    def test_add_client_success(self):
        c.client_list = []
        cm.add_client('Gabe', 'Cruz', 'test@gmail.com', '0487362360')
        self.assertEqual(c.client_list[0].name, 'Gabe')
        self.assertEqual(c.client_list[0].surname, 'Cruz')
        self.assertEqual(c.client_list[0].email, 'test@gmail.com')
        self.assertEqual(c.client_list[0].contact_number, '0487362360')

    def test_empty_values(self):
        with self.assertRaises(TypeError):
            cm.add_client('Test One', 'test.com', 4)
            cm.add_client('Gabe', 4)
            cm.add_client('Test', 'test@g.c')


class TestRemoveClient(test.TestCase):
    def setUp(self):
        super(TestRemoveClient, self).setUp()
        self.addTypeEqualityFunc(str, self.assertMultiLineEqual)

    def test_remove_client_success(self):
        c.client_list = []
        cm.add_client('Gabe', 'Cruz', 'test@gmail.com', '0487362360')
        cm.add_client('Chris', 'Daniels', 'test2@gmail.com', '0479365112')

        #testing with old version of addClient
        self.assertRaises(TypeError, cm.remove_client, 'Gabe', 'Cruz')

        #remove one from list
        client_remove_test = [x for x in c.client_list if x.name == 'Gabe' and x.surname == 'Cruz']
        cm.remove_client(client_remove_test[0].client_id)

        """
        we add client_id at end of expected
        because the users cannot set the id
        the program auto-generates the client id
        so we must get the value
        """
        actual = c.client_list[0].full_info()
        expected = f"Chris Daniels, test2@gmail.com, 0479365112, {c.client_list[0].client_id}"
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            expected2 = "Gabe Cruz, test@gmail.com, 0487362360"
            self.assertEqual(actual, expected2)


if __name__ == "__main__":
    test.main()
