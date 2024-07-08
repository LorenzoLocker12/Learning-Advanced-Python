from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

search_bar_input = driver.find_element(By.NAME, 'search')
search_bar_button = driver.find_element(By.XPATH, '//*[@id="p-search"]/a')

search_bar_button.click()
search_bar_input.send_keys("Python")
search_bar_input.send_keys(Keys.ENTER)


