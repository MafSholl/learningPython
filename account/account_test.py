import unittest
from . import account


class MyTestCase(unittest.TestCase):
    def test_that_account_can_be_created(self):
        account1 = account.Account()
        self.assertIsNotNone(account1)
        self.assertIsInstance(account1, account.Account)

    def test_that_account_has_a_name(self):
        """
        GIVEN: I have an account
        wHEN: I ask for the name
        THEN: Give me the name
        """
        account1 = account.Account()
        name = account1.name
        self.assertEqual("Tolani", name)

    def test_that_account_can_deposit(self):
        account1 = account.Account()
        account1.deposit(2000)
        self.assertEqual(2000, account1.balance)

    def test_that_negative_deposit_is_declined(self):
        account1 = account.Account()
        self.assertEqual(0, account1.balance)
        account1.deposit(500)
        # account1.deposit(-1000)
        self.assertEqual(500, account1.balance)

    def test_that_negative_deposit_raises_error(self):
        account1 = account.Account()
        account1.deposit(500)
        self.assertRaises(ValueError, account1.deposit, -1000)
        self.assertEqual(500, account1.balance)

    def test_that_account_can_withdraw(self):
        account1 = account.Account()
        account1.deposit(2000)
        account1.withdraw(1000)
        self.assertEqual(1000, account1.balance)

    def test_that_negative_amount_cannot_be_withdrawn(self):
        account1 = account.Account()
        account1.deposit(2000)
        self.assertRaises(ValueError, account1.withdraw, -1000)
        self.assertEqual(2000, account1.balance)

    def test_that_airtime_can_be_bought(self):
        account1 = account.Account()
        account1.deposit(5000)
        account1.airtime_purchase(1000)
        self.assertEqual(4000, account1.balance)

    def test_that_negative_airtime__amount_cannot_be_bought(self):
        account1 = account.Account()
        account1.deposit(5000)
        self.assertRaises(ValueError, account1.airtime_purchase, -1000)
        self.assertEqual(5000, account1.balance)

    def test_that_account_can_transfer(self):
        account1 = account.Account()
        account2 = account.Account()
        account1.deposit(10000)
        account1.transfer(5000, account2)
        self.assertEqual(5000, account1.balance)
        self.assertEqual(5000, account2.balance)





if __name__ == '__main__':
    unittest.main()
