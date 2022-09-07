import unittest
import basket_voucher

class MyTestCase(unittest.TestCase):
    def test_that_basket_exist(self):
        basket1 = basket_voucher.Basket()
        self.assertIsNotNone(basket1)
        self.assertIsInstance(basket1, basket_voucher.Basket)

    def test_that_basket_add_item(self):
        basket1 = basket_voucher.Basket()
        basket1.add("Wristwatch")
        self.assertEqual("Wristwatch", basket1.find("Wristwatch"))

    def test_that_basket_cannot_take_more_than_three_items(self):
        basket1 = basket_voucher.Basket()
        basket1.add("Wristwatch")
        basket1.add("Sneakers")
        basket1.add("Deodorant")
        self.assertRaises(IndexError, basket1.add, "Books")

    def test_that_basket_can_item_with_price(self):
        basket1 = basket_voucher.Basket()
        basket1.add("Wristwatch", 3000)
        self.assertEqual("Wristwatch", basket1.find("Wristwatch"))
        self.assertEqual(7000, basket1.wallet)

    def test_that_basket_cannot_add_item_with_insufficient_wallet_balance(self):
        basket1 = basket_voucher.Basket()
        basket1.add("Wristwatch", 3000)
        basket1.add("Sneakers", 6000)
        self.assertRaises(ValueError, basket1.add, "Books", 4000)

    def test_that_basket_cannot_add_more_than_three_item__even_with_sufficient_wallet_balance(self):
        basket1 = basket_voucher.Basket()
        basket1.add("Wristwatch", 3000)
        basket1.add("Sneakers", 3000)
        basket1.add("Deodorant", 2000)
        self.assertRaises(IndexError, basket1.add, "Books", 1000)


if __name__ == '__main__':
    unittest.main()
