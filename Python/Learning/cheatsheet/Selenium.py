"""
Selenium Python Cheat Sheet
Covers classes, methods, functions, locators, waits, interactions, and common patterns.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# -----------------------------
# 1. INITIALIZE DRIVER
# -----------------------------
driver = webdriver.Chrome()  # You can also use Firefox(), Edge(), etc.
driver.get("https://example.com")  # Open URL

# -----------------------------
# 2. LOCATING ELEMENTS
# -----------------------------
# By ID
element = driver.find_element(By.ID, "element_id")

# By Name
element = driver.find_element(By.NAME, "element_name")

# By Class Name
element = driver.find_element(By.CLASS_NAME, "class_name")

# By Tag Name
element = driver.find_element(By.TAG_NAME, "tag")

# By CSS Selector
element = driver.find_element(By.CSS_SELECTOR, ".myclass #id")

# By XPath
element = driver.find_element(By.XPATH, "//div[@id='myid']")

# -----------------------------
# 3. MULTIPLE ELEMENTS
# -----------------------------
elements = driver.find_elements(By.CLASS_NAME, "common_class")  # returns list

# -----------------------------
# 4. INTERACTING WITH ELEMENTS
# -----------------------------
element.send_keys("Hello")  # type into input

element.click()               # click button or link

element.clear()               # clear text input

# Press special keys
element.send_keys(Keys.ENTER)
element.send_keys(Keys.TAB)

# -----------------------------
# 5. GETTING INFO FROM ELEMENTS
# -----------------------------
text = element.text                     # visible text
attribute_value = element.get_attribute("href")  # attribute
is_displayed = element.is_displayed()  # check visibility
is_enabled = element.is_enabled()      # check if enabled

# -----------------------------
# 6. WAITING FOR ELEMENTS
# -----------------------------
# Explicit Wait
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "element_id"))
    )
except TimeoutException:
    print("Element not found within 10 seconds")

# Implicit Wait
driver.implicitly_wait(5)  # waits up to 5 seconds for elements

# -----------------------------
# 7. NAVIGATION
# -----------------------------
driver.back()
driver.forward()
driver.refresh()

# -----------------------------
# 8. ALERTS & FRAMES
# -----------------------------
# Switch to alert
# alert = driver.switch_to.alert
# alert.accept() or alert.dismiss()

# Switch to iframe
# driver.switch_to.frame("frame_name_or_id")
# driver.switch_to.default_content()

# -----------------------------
# 9. SCROLLING & EXECUTING JS
# -----------------------------
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# -----------------------------
# 10. COOKIES
# -----------------------------
cookies = driver.get_cookies()
driver.add_cookie({"name": "key", "value": "value"})
driver.delete_cookie("key")
driver.delete_all_cookies()

# -----------------------------
# 11. SCREENSHOTS
# -----------------------------
driver.save_screenshot("screenshot.png")
driver.get_screenshot_as_file("screenshot2.png")

# -----------------------------
# 12. CLOSING BROWSER
# -----------------------------
driver.close()   # closes current tab

driver.quit()    # closes entire browser session

# -----------------------------
# 13. EXCEPTIONS
# -----------------------------
# NoSuchElementException, TimeoutException, ElementNotInteractableException, WebDriverException

# -----------------------------
# END OF CHEATSHEET
# -----------------------------