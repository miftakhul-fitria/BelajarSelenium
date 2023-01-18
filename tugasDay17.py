import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # TESCT CASE 1
    def test_a_success_login(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://www.saucedemo.com/")  # buka situs
        time.sleep(3)
        browser.find_element(
            By.ID, "user-name").send_keys("standard_user")  # isi username
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys(
            "secret_sauce")  # isi password
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "login-button").click()
        time.sleep(1)

    # TESCT CASE 2
    def test_a_failed_login_with_empty_password(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://www.saucedemo.com/")  # buka situs
        time.sleep(3)
        browser.find_element(
            By.ID, "user-name").send_keys("standard_user")  # isi username
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys(
            "")  # isi password
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "login-button").click()
        time.sleep(1)

    # TESCT CASE 3
    def test_a_failed_login_with_empty_email_and_password(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://www.saucedemo.com/")  # buka situs
        time.sleep(3)
        browser.find_element(
            By.ID, "user-name").send_keys("")  # isi username
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys(
            "")  # isi password
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "login-button").click()
        time.sleep(1)

    # TESCT CASE 4
    def test_a_failed_login_with_wrong_password(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://www.saucedemo.com/")  # buka situs
        time.sleep(3)
        browser.find_element(
            By.ID, "user-name").send_keys("standard_user")  # isi username
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys(
            "miftakhulfitria")  # isi password
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "login-button").click()
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()