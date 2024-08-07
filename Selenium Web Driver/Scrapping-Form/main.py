from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, "fName")
l_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
signup_button = driver.find_element(By.XPATH, "/html/body/form/button")

f_name.send_keys("Lorenzo")
l_name.send_keys("Locker")
email.send_keys("example@gmail.com")
signup_button.click()

