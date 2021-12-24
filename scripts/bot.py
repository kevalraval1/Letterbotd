from selenium import webdriver

PATH = "/Users/Keval/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://letterboxd.com/")
print(driver.title)
driver.quit()
