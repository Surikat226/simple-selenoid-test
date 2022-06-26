import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_search_in_google(browser):
	browser.get("https://www.google.ru/")

	search_field = browser.find_element(By.CSS_SELECTOR, "[title='Поиск']")
	time.sleep(2)
	search_field.send_keys("В чём сила, брат?")
	time.sleep(2)
	search_field.send_keys(Keys.ENTER)

	time.sleep(2)
	browser.close()