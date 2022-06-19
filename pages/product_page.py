from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_basket_btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        add_basket_btn.click()

    def get_purchase_value(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_value = product.text
        print(f"Product: {product_value}\n")
        return product_value

    def get_price_value(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price_value = price.text
        print(f"Price: {price_value}\n")
        return price_value

    def should_be_equal_product(self, product_name):
        added_product_name = self.browser.find_element(
            *ProductPageLocators.ADDED_PRODUCT_NAME)
        print(f"Added product: {added_product_name.text}\n")
        assert product_name == added_product_name.text, "Product name not equal added product"

    def should_be_equal_price(self, price_name):
        added_product_price = self.browser.find_element(
            *ProductPageLocators.ADDED_PRODUCT_PRICE)
        print(f"Added price: {added_product_price.text}\n")
        assert price_name == added_product_price.text, "Price name not equal added price"
