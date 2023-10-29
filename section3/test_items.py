from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_exists(browser):
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    time.sleep(2)
    assert button

