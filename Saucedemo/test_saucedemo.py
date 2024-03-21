# 1 - Librairies
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Class Definition ?(it is optional to use the class)
class Teste_Produtos():

    # 2.1 Attributs
    url = "https://www.saucedemo.com"              # endereço do site alvo

    # 2.2 Functions / Methods
    def setup_method(self, method):                # method to initialize the test
        self.driver = webdriver.Chrome()           # is a web browser driver for Google Chrome
        self.driver.implicitly_wait(10)            # wait for any element up to 10 seconds

    def teardown_method(self, method):             # method to finalize the test
        self.driver.quit()                         # close the browser and end the session

    def test_select_produt(self):                  # method to test the selection of a product
        self.driver.get(self.url)                  # open the website
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")             # type the username
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")             # type the password
        self.driver.find_element(By.ID, "login-button").click()                             # click on the login button                                                                  
        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"                # Assert Products / I used CCS_SELECTOR to asserts
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text == "Sauce Labs Backpack"                       # and I used ID to click on the element
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(N) .inventory_item_price").text == "$29.99"      # assert the price of the product
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()                                              # click on the add to cart button
        assert self.driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > .shopping_cart_link').text == "1"    
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Your Cart"
        assert self.driver.find_element(By.CSS_SELECTOR, '.inventory_item_name').text == "Sauce Labs Backpack"
        assert self.driver.find_element(By.CSS_SELECTOR, '.inventory_item_price').text == "$29.99"
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
        

             