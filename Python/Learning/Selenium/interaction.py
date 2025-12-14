from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.udemy.com/course/100-days-of-code/learn/lecture/21785306#content")

CourseTitle = driver.find_element(By.CLASS_NAME, "truncate-with-tooltip--ellipsis--YJw4N ")
print(CourseTitle.text)