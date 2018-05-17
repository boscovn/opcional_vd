from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Firefox()
driver.get("https://twitter.com/login")
user = driver.find_element_by_class_name("js-username-field")
password = driver.find_element_by_class_name("js-password-field")
user.send_keys("edgelord_xxx")
password.send_keys("1234asdF")
driver.find_element_by_class_name("EdgeButtom--medium").click()
tweet=driver.find_element_by_id("tweet-box-home-timeline")
tweet.send_keys("Estoy usando selenium")
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.tweet-action')))
driver.implicitly_wait(10)
element.click()
#tweet-action EdgeButton EdgeButton--primary js-tweet-btn