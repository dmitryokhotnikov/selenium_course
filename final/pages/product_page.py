from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

    def check_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert self.get_basket_product_name() == product_name, "product name and his name in basket are different"

    def check_product_cost(self):
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        assert self.get_basket_product_cost() == product_cost, "product cost and his cost in basket are different"

    def get_basket_product_name(self):
        basket_messages = self.browser.find_elements(*ProductPageLocators.BASKET_MESSAGES)
        return basket_messages[0].text

    def get_basket_product_cost(self):
        basket_messages = self.browser.find_elements(*ProductPageLocators.BASKET_MESSAGES)
        return basket_messages[2].text


