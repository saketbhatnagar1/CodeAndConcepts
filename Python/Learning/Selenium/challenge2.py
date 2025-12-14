from selenium import webdriver
from selenium.webdriver.common.by import By

dirver = webdriver.Chrome()
dirver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = dirver.find_element(By.NAME, "fName")
last_name = dirver.find_element(By.NAME, "lName")
email = dirver.find_element(By.NAME, "email")

first_name.send_keys("Saket")
last_name.send_keys("Bhatnagar")
email.send_keys("saketbhatnagar2@gmail.com")

submit = dirver.find_element(By.CSS_SELECTOR, "form button")
submit.click()