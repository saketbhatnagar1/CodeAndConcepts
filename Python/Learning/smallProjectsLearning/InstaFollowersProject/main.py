from selenium import webdriver
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(ENV_PATH)

username = "subject8481"  # os.getenv("USERNAME")
password = os.getenv("PASSWORD")

print(username, password)

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        # stable selectors
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")
        login_button   = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

    def find_followers(self):
        pass

    def follow(self):
        pass

bot = InstaFollower()
bot.login(username, password)
