from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options);
driver.get("https://python.org")


events_name = driver.find_elements(By.CSS_SELECTOR, '.event-widget .menu a')
events_time = driver.find_elements(By.CSS_SELECTOR, '.event-widget .menu time')

events_dict = {}
for i in range(len(events_name)):
    events_dict[i] = {
        "time": events_time[i].text,
        "name": events_name[i].text
    }
print(events_dict)





driver.quit()