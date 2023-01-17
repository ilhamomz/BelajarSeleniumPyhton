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
        browser.get("https://www.saucedemo.com/")
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR,"input#user-name").send_keys("standard_user")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html//input[@id='password']").send_keys("secret_sauce")
        time.sleep(2)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(2)

    def tearDown(self): 
        self.browser.close() 