from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://www.wikipedia.org/")
driver.maximize_window()

driver.implicitly_wait(5)
wait = WebDriverWait(driver, 5)

wait.until(EC.visibility_of_element_located((By.ID, "www-wikipedia-org")))

search = driver.find_element(By.XPATH, '//*[@id="searchInput"]')
search.send_keys("Croatia")
driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button/i').click()

# verify correct URL

CroatURL = "https://en.wikipedia.org/wiki/Croatia"
if driver.current_url == CroatURL:
    print("URL is correct")

driver.find_element(By.XPATH, '//*[@id="pt-login"]/a/span').click()
driver.implicitly_wait(1.5)

Username = driver.find_element(By.XPATH, '//*[@id="wpName1"]')
Username.send_keys("AnnaFlow")
Password = driver.find_element(By.XPATH, '//*[@id="wpPassword1"]')
Password.send_keys("Kjelka_7")
driver.find_element(By.XPATH, '//*[@id="wpLoginAttempt"]').click()

driver.get_full_page_screenshot_as_png()

# verifies user is logged in

if "AnnaFlow" not in driver.page_source:
    pass
else:
    print("User is logged in")

driver.quit()
