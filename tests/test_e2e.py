from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_saucedemoe2e(driver):
    driver.get("https://www.saucedemo.com")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    assert products_page.get_title() == "Products"

    products_page.add_bagpack_to_cart()
    assert products_page.get_cart_count() == "1"

    print ("End to End Test passed!")