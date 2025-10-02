import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.product_page import ProductPage


class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper.get_driver(
            "https://www.terminalx.com/brands/tx-collabs/margaux-jane/w655950008?color=7"
        )

    def test_add_product_to_cart(self):
        product_page = ProductPage(self.browser)

        # שלב 1: לבחור מידה M
        product_page.select_size_m()

        # שלב 2: להוסיף לעגלה
        product_page.add_to_cart()

        # שלב 3: בדיקות על המיני-קארט
        product_name = product_page.get_minicart_product_name()
        size = product_page.get_minicart_size()
        color = product_page.get_minicart_color()
        price = product_page.get_minicart_price()
        qty = product_page.get_minicart_qty()

        print(f"Product: {product_name}, Size: {size}, Color: {color}, Price: {price}, Qty: {qty}")

        self.assertIn("סריג ניקי", product_name, " Product name is wrong in minicart")
        self.assertEqual(size, "M", " Size is not correct in minicart")
        self.assertEqual(color, "אפור", " Color is not correct in minicart")
        self.assertIn("169.90", price, " Price is not correct in minicart")
        self.assertEqual(qty, "1", " Quantity is not correct in minicart")

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
