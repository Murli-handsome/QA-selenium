from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
driver.get("http://www.canadanepal.com")

# assert "canada" in driver.title

elem = driver.find_element(By.NAME,"keyword")
elem.clear()
elem.send_keys("कबाब")
elem.send_keys(Keys.RETURN)
time.sleep(1000)

assert "No results found." not in driver.page_source
driver.close()


