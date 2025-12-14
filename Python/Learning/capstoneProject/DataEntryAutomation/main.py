import os
import re
import time
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ---------------- LOAD ENV ----------------
load_dotenv()
WEBSITE = os.environ.get("WEBSITE")
FORM_LINK = os.environ.get("FORM_LINK")

# ---------------- SCRAPE DATA ----------------
header = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }
response = requests.get(WEBSITE,headers=header)
soup = BeautifulSoup(response.text, "html.parser")

# Prices
prices = soup.find_all("span", attrs={"data-test": "property-card-price"})
price_list = [
    int(re.sub(r"[^\d]", "", price.get_text()))
    for price in prices
]

# Addresses
addresses = soup.find_all("address")
address_list = [
    " ".join(addr.get_text().split())
    for addr in addresses
]

# Links
links = soup.find_all("a", attrs={"data-test": "property-card-link"})
links_list = [
    link.get("href")
    for link in links
]

# ---------------- SELENIUM SETUP ----------------
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

# ---------------- FILL FORM ----------------
for i in range(min(len(address_list), len(price_list), len(links_list))):

    driver.get(FORM_LINK)

    inputs = wait.until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, "input[jsname='YPqjbf']")
        )
    )

    # Scroll into view
    for inp in inputs:
        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", inp
        )
        time.sleep(0.2)

    # Fill fields
    inputs[0].click()
    inputs[0].send_keys(address_list[i])

    inputs[1].click()
    inputs[1].send_keys(str(price_list[i]))

    inputs[2].click()
    inputs[2].send_keys(links_list[i])

    # Submit
    # submit_button = wait.until(
    #     EC.element_to_be_clickable(
    #         (By.XPATH, "//span[text()='Submit']")
    #     )
    # )
    # submit_button.click()
    submit_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='button']")
        )
    )
    submit_button.click()
    time.sleep(2)  # avoid form spam detection

driver.quit()
