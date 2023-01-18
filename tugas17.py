import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        

    def test_login_sukses(self):

        browser = self.browser
        browser.get("https://www.saucedemo.com")
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR,"input#user-name").send_keys("standard_user")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='password']").send_keys("secret_sauce")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)

    def test_gagal_login_username_password_kosong(self):
        browser = self.browser 
        browser.get("https://www.saucedemo.com") 
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@id='user-name']").send_keys("") 
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() 
        time.sleep(1)

    def test_gagal_login_password_kosong(self):
        browser = self.browser 
        browser.get("https://www.saucedemo.com") 
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@id='user-name']").send_keys("standard_user") 
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() 
        time.sleep(1)

    def test_gagal_login_salah_password(self):
        browser = self.browser 
        browser.get("https://www.saucedemo.com") 
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@id='user-name']").send_keys("standard_user") 
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("aaaaa")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() 
        time.sleep(1)

    def test_add_chart(self):
        browser = self.browser
        browser.get("https://www.saucedemo.com")
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR,"input#user-name").send_keys("standard_user")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='password']").send_keys("secret_sauce")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)
        browser.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"div#shopping_cart_container > .shopping_cart_link").click()
        time.sleep(1)
        browser.find_element(By.ID,"checkout").click()
        time.sleep(1)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()