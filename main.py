from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\webdriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

while True:
	driver.get('https://www.youtube.com')

	search = driver.find_element_by_name("search_query")
	search.send_keys("Ryan")
	button = driver.find_element_by_id("search-icon-legacy")
	button.click()
	time.sleep(2)

	for x in range(4):
		search = driver.find_element_by_name("search_query")
		search.send_keys(Keys.BACK_SPACE)

	logo = driver.find_element_by_id("logo-icon-container")
	logo.click()

	time.sleep(2)