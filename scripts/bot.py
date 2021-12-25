"""
TODO:
1. Integrate with movie API
2. User Input available
3. GUI
4. Voice to words input
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "/Users/Keval/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://letterboxd.com/")
print(driver.title)
driver.quit()
driver.get("https://letterboxd.com/sign-in/")

username = driver.find_element_by_id("signin-username").send_keys("kevalraval")

password = driver.find_element_by_id("signin-password").send_keys("passwordhere")

submit = driver.find_element_by_class_name("button-container").click()

try:
    element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "add-new-button"))
    )
finally:
    log = driver.find_element_by_id("add-new-button").click()

try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.ID, "frm-film-name"))
    )
finally:
    time.sleep(1)
    driver.find_element_by_id("frm-film-name").send_keys("The Dark Knight (2008)") # film name should be user input, year should be queried from IMDB
    # Will make this dynamic based on user input, should be able to query for a year for the movie and add it to search result

try:
    element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ac_even"))
    )
finally:
    result = driver.find_element_by_class_name("ac_even").click()

try:
    element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "frm-review"))
    )
finally:
    time.sleep(1)
    review = driver.find_element_by_id("frm-review").send_keys("Test Review")

driver.find_element_by_class_name("needsclick").click()

tags = driver.find_element_by_name("tags")

taglist = ['disney', 'nolan', 'superhero', 'batman', 'dark knight', '2008'] # Should be dynamic based on query from IMDb api

for tag in taglist:
    tags.send_keys(tag)
    tags.send_keys(Keys.RETURN)


# 12.5 pixels = half a star, click happens at center so 2.5 stars is 0 pixels
def getRating(rating):
    return (rating * 25 - 62.5)

ac = ActionChains(driver)
rating = driver.find_element_by_id("rateit-range-2")
ac.move_to_element(rating).move_by_offset(getRating(2.5), 0).click().perform()

driver.find_element_by_id("film-like-checkbox").click() # Liking should be optional

driver.find_element_by_id("contains-spoilers").click() #spoilers should be optional

driver.find_element_by_id("diary-entry-submit-button").click()