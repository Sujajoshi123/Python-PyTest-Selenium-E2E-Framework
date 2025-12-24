from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):
    TITLE = (By.CLASS_NAME,"title")

    ADD_BAGPACK_BTN = ( By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def get_title(self):
        return self.get_text(self.TITLE)
    

    def add_bagpack_to_cart(self):
        self.click_element(self.ADD_BAGPACK_BTN)

    def get_cart_count(self):
        return self.get_text(self.CART_BADGE)